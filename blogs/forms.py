from django import forms
from .models import Blog, BlogComment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content", "published_date")
        
class BlogCommentForm(forms.Form):
    Blog_comment = forms.CharField(100)