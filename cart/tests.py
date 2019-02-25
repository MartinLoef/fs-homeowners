from django.test import TestCase
from .views import adjust_cart

# Create your tests here.
class CartTests(TestCase):
    print('Running Cart Tests')
    def test_get_cart(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        
        
    def test_change_item_number(self):
        product = Product(
            id = 7,
            setnumber = '42',
            name = 'Zephod',
            category = 'Beeblebrox',
            price = '3.25',
            )
        product.save()
        id = product.id
        cart_items = [{7: 2}]
        cart = {}
        quantity = 3
        cart[id] = quantity
        response = self.client.post('/cart/adjust_cart {0}'.format(product.id), {'cart_items':cart_items,'quantity':quantity})
        self.assertEqual(cart, {7: 3})
        

        