from django import forms

class ContactForm(forms.Form):
    """ Simple straight-forward form
    """
    contact_name = forms.CharField(label='Name', required=True)
    contact_email = forms.EmailField(label='Email Address', required=True)
    subject = forms.CharField(label='Subject', required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)