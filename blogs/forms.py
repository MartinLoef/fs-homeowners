from django import forms
from .models import Blog, BlogComment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["author", "views"]
        
        
class BlogCommentForm(forms.Form):
    Blog_comment = forms.CharField(125)