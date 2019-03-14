from django.test import TestCase
from .forms import BlogPostForm, BlogCommentForm
from django.contrib.auth.models import User
from .models import Blog, BlogComment
# Create your tests here.
class TestDjango(TestCase):
        
    def test_BlogPostForm_form_valid(self):
        User.objects.create(username="Martin")
        form = BlogPostForm({
            'author': User.objects.get(username="Martin").pk,
            'title': 'Automated Test',
            'content': 'This is a test',
            'blog_image': 'images/monkeytest.jpg',
            'views': '0',
        })
        
        self.assertTrue(form.is_valid())
        
