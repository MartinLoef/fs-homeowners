from django.conf.urls import url
from .views import create_or_edit_event, get_events

urlpatterns = [
    url(r'^events/$', get_events, name="get_events"),
    url(r'^new/$', create_or_edit_event, name='new_event'),
    ]