from django.conf.urls import url
from .views import create_or_edit_event, get_events, event_detail, event_like

urlpatterns = [
    url(r'^events/$', get_events, name="get_events"),
    url(r'^(?P<pk>\d+)/$', event_detail, name='event_detail'),
    url(r'^new/$', create_or_edit_event, name='new_event'),
    url(r'^(?P<pk>\d+)/like/$', event_like, name='event_like'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_event, name='edit_event'),
    ]