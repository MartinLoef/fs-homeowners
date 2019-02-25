from django import forms
from .models import Order
from datetime import datetime, timedelta

class PaymentForm(forms.Form):
    """
    Form to obtain payment information for credit card.
    Expiration motnh and year progress yearly based on 'now'
    """
    _this_year = int(
        datetime.now().strftime("%Y")
        )
    _end_year = int(
        (datetime.now() + timedelta(weeks=1040)
        ).strftime("%Y"))
    
    MONTH_CHOICES = [(i,i) for i in range(1,13)]
    YEAR_CHOICES = [(i,i) for i in range(_this_year, _end_year)]
    
    credit_card_number = forms.CharField(
        label='Credit Card Number',
        required=False,
        )
    cvv = forms.CharField(
        label='CVV Code', 
        required=False,
        )
    expiry_month = forms.ChoiceField(
        label='Expiration Month', 
        choices=MONTH_CHOICES, 
        required=False,
        )
    expiry_year = forms.ChoiceField(
        label='Expiration Year', 
        choices=YEAR_CHOICES, 
        required=False,
        )
    stripe_id = forms.CharField(
        widget=forms.HiddenInput,
        )
    
class OrderForm(forms.ModelForm):
    """
    Standard form with modified label names
    """
    class Meta:
        model = Order
        
        labels = {
            'full_name':'Full Name',
            'address1':'Address Line 1',
            'address2':'Address Line 2',
            'town_or_city':'Town or City',
            'state_or_province':'State or Province',
            }
        
        fields = (
            'full_name', 
            'address1', 
            'address2', 
            'postcode', 
            'town_or_city', 
            'state_or_province', 
            'country', 
            'phone_number',
            'email_address',
            )