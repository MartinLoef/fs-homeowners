from django.test import TestCase
from .views import adjust_cart

# Create your tests here.
class CartTests(TestCase):
    print('Running Cart Tests')
    def test_get_cart(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        
        
    
        

        