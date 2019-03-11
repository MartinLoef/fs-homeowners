from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """
    Process the contact form and send mails to admins,
    as well as the submitter of the form.
    """
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                """ Send form to site admins
                """
                message = render_to_string(
                    'contact_mail.html',{
                        'contact_name':form.cleaned_data['contact_name'],
                        'contact_email':form.cleaned_data['contact_email'],
                        'form_subject': form.cleaned_data['subject'],
                        'form_content': form.cleaned_data['content'],
                    })
                mail_subject = 'Contactform: ' + form.cleaned_data['subject']
                email_to = 'commonholdproject@gmail.com'
                email = EmailMessage(
                    mail_subject, message, to=[email_to])
                email.content_subtype = 'html'
                email.send()
                
                messages.error(request, 
                    'Thank you for your mail!'
                    + ' We\'ll get back to you as soon as possible!')
                return redirect('index')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                    
    return render(request, 'contact.html', {
        'form':form,
        })
