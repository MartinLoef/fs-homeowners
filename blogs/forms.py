from django import forms
from .models import Blog, BlogComment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["authorid", "views"]
        
        
class BlogCommentForm(forms.Form):
    Blog_comment = forms.CharField(max_length=125, label=False)