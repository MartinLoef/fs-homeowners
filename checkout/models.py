from django.db import models
from events.models import Event
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    full_name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=40, blank=False)    
    address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    state_or_province = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.EmailField(max_length=40, blank=False, default='')
    date = models.DateField()
    
    def __str__(self):
        return "OrderID: {0} / Date: {1} / User: {2}".format(
            self.id, self.date, self.user)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    event = models.ForeignKey(Event, null=False)
    quantity = models.IntegerField(blank=False)
    total_item_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    @property
    def get_total_item_price(self):
        return self.event.price*self.quantity
    
    def __str__(self):
        self.total_item_price = self.get_total_item_price
        return "Qty: {0} / Item: {1} @ € {2} / Total: € {3} / OrderID: {4}".format(
            self.quantity, 
            self.event.title, self.event.price, 
            self.total_item_price,
            self.order.id
            )
