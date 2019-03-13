from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
# Create your tests here.
class TestDjango(TestCase):
        
    def test_UserLogin_form_valid(self):
        form = UserLoginForm({
            'username': 'daisy',
            'password': 'Password123',
            
        })

        self.assertTrue(form.is_valid())
        
    def test_UserRegistrationForm_form_valid_mandatory_fields(self):
        form = UserRegistrationForm({
            'email': 'martin@loef.nl',
            'password1': 'Password123',
            'password2': 'Password123',
            'username': 'martin'
        })
        self.assertTrue(form.is_valid())
    
    