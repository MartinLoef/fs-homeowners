from django.conf.urls import url, include
from accounts.views import index, logout, SignIn, registration, accounts, overview, user_suspend, user_activate
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^overview/$', overview, name="overview"),
    url(r'^SignIn/$', SignIn, name="SignIn"),
    url(r'^register/$', registration, name="registration"),
    url(r'^password_reset/', include(url_reset)),
    url(r'^accounts/$', accounts, name='accounts'),
    url(r'^suspend/(?P<pk>\d+)$', user_suspend, name='suspend'),
    url(r'^activate/(?P<pk>\d+)$', user_activate, name='activate'),
]