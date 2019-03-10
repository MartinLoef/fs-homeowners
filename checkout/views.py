from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import Order, OrderItem
from django.conf import settings
from django.utils import timezone
from events.models import Event
from .models import User
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    """
    Validation and processing of the form(s) filled out
    within the checkout submission.
    """
    if request.method=='POST':
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = User.objects.get(pk=request.user.id) 
            order.save()
            saved_order = get_object_or_404(Order, pk=order.id)
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                event = get_object_or_404(Event, pk=id)
                total_item_price = quantity * event.price
                total += quantity * event.price
                order_item = OrderItem(
                    order = order,
                    event = event,
                    quantity = quantity,
                    total_item_price = total_item_price,
                    )
                order_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = order_form.cleaned_data['email_address'],
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, 
                    'Your payment failed, your card was declined.'
                    )
                
            if customer.paid:
                try:
                    order_items = OrderItem.objects.filter(order=saved_order)
                    site = get_current_site(request)
                    message = render_to_string(
                        'confirmation.html',{
                            'order':saved_order,
                            'order_items':order_items,
                            'total': total,
                            'site':site.domain,
                        })
                    mail_subject = 'Thank you for your order'
                    email_to = order_form.cleaned_data['email_address']
                    email = EmailMessage(mail_subject, message, to=[email_to])
                    email.content_subtype = 'html'
                    email.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                
                messages.error(request, 
                    'Your order has been placed.'
                    + ' A confirmation email should arrive shortly.')
                request.session['cart'] = {}
                
                return redirect(reverse('get_events'))
            else:
                messages.error(request, 
                    'Unable to take payment at this time, '
                    + 'please try again later')
        else:
            messages.error(request, 
                'We were unable to take a payment with the card you put in')
    else:
        payment_form = PaymentForm()
        order_form = OrderForm()
        
    return render(request, 'checkout.html', {
        'order_form': order_form, 
        'payment_form':payment_form, 
        'stripe_publishable':settings.STRIPE_PUBLISHABLE}
        )
