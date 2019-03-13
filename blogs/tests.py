from django.test import TestCase
from .forms import BlogPostForm, BlogCommentForm
# Create your tests here.
class TestDjango(TestCase):
        
    def test_BlogPostForm_form_valid(self):
        form = BlogPostForm({
            'author': 'admin',
            'title': 'Automated Test',
            'content': 'This is a test',
            'blog_image': 'images/monkeytest.jpg',
            'published_date': '2019-03-13',
            'views': '0',
            
        })

        self.assertTrue(form.is_valid())
        
    def test_BlogCommentForm(self):
        form = BlogCommentForm({
            'blogid': '1',
            'authorid': 'admin',
            'blog_comment': 'Comment test',
            'created_date': '2019-03-13'
        })
        self.assertTrue(form.is_valid())