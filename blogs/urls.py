from django.conf.urls import url
from .views import get_blogs, blog_detail, create_or_edit_blog, blog_like

urlpatterns = [
    url(r'^blogs/$', get_blogs, name="get_blogs"),
    url(r'^(?P<pk>\d+)/$', blog_detail, name='blog_detail'),
    url(r'^(?P<pk>\d+)/like/$', blog_like, name='blog_like'),
    url(r'^new/$', create_or_edit_blog, name='new_blog'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_blog, name='edit_blog')
    ]