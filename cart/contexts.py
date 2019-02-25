from django.shortcuts import get_object_or_404
from events.models import Event


def cart_contents(request):
    """
    Make cart contents available when rendering any page
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        event = get_object_or_404(Event, pk=id)
        total += quantity * event.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'event': event})
    
    return { 'cart_items': cart_items, 'total': total, 
        'product_count': product_count }