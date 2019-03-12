from django.conf.urls import url
from .views import checkout, orderhistory

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^order/$', orderhistory, name='orderhistory'),
    ]