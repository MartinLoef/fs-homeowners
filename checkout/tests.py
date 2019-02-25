from django.test import TestCase
from .forms import OrderForm, PaymentForm
from datetime import datetime, timedelta

class CheckoutFormTests(TestCase):
    def test_orderform_isvalid(self):
        form = OrderForm({
            'full_name':'Clint Barton',
            'address1':'Secluded 12',
            'address2':'',
            'postcode':'',
            'town_or_city':'Farawayville',
            'state_or_province':'',
            'country':'United States',
            'phone_number':'555-12345',
            'email_address':'clint@avengers.hq',
        })
        self.assertTrue(form.is_valid())

    
    def test_paymentform_isvalid(self):
        """make a variable end year for perpetual validity"""
        _end_year = int(
            (datetime.now() + timedelta(weeks=520)
            ).strftime("%Y"))
            
        form = PaymentForm({
            'credit_card_number':'424242424242',
            'cvv':'111',
            'expiry_month':'11',
            'expiry_year':_end_year,
            'stripe_id':'sk_test_loadofcharacters'
        })
        self.assertTrue(form.is_valid())