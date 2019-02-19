from django.conf.urls import url, include
from accounts.views import index, logout, SignIn, registration, profile, accounts, user_profile, overview
from accounts import url_reset
from accounts import views

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^overview/$', overview, name="overview"),
    url(r'^SignIn/$', SignIn, name="SignIn"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="user_profile"),
    url(r'^password_reset/', include(url_reset)),
    url(r'^accounts/$', accounts, name='accounts'),
]