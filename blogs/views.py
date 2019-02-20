from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, BlogComment, BlogLike, User
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required

def get_blogs(request):
    """blogposts.html"""
    
    return render(request, "blogposts.html")
    
def blog_like(request, pk):
    """blogdetail.html"""
    return redirect(blog_detail)
    
def blog_detail(request, pk):
    """blogdetail.html"""
    return render(request, "blogposts.html")
    
def create_or_edit_blog(request, pk=None):
    """blogpostform.html"""
    return render(request, "blogpostform.html")
    