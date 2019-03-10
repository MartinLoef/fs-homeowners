from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


""" custom imports """
from .models import Blog, BlogComment, BlogLike, User
from accounts.models import UserProfile
from .forms import BlogPostForm, BlogCommentForm


def get_blogs(request):
    """ 
    get all the blogposts if the user is logged in
    """
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, "blogposts.html", {'blogs': blogs})
    else:
        return redirect(reverse('index'))
   
@login_required
def blog_like(request, pk):
    """
    users can like or remove an earlier 
    given like on a blog
    """
    if request.user.is_authenticated:
        users = User.objects.all()
        blogid = Blog.objects.get(pk=pk)
        userid = User.objects.get(pk=request.user.id)
        
        likes = BlogLike.objects.filter(BlogLikeId=pk)
        comment_form = BlogCommentForm()
        
        if likes:
            for like in likes:
                if like.BlogLikedBy == userid:
                    BlogLike.objects.filter(BlogLikeId=blogid, 
                                            BlogLikedBy=userid).delete()
                    thumb = False
                else:
                    BlogLike.objects.create(BlogLikeId=blogid, 
                                            BlogLikedBy=userid) 
                    thumb = True
        else:
            BlogLike.objects.create(BlogLikeId=blogid, BlogLikedBy=userid)
            thumb = True
       
        return HttpResponseRedirect(reverse('blog_detail', args=(pk,)))
    else:
        messages.success(request, "You are supposed to be logged in to like that!")
        return redirect(reverse('index'))
        
def blog_detail(request, pk):
    """
    request the blog detail page
    post possibilitie for comments on the blog
    """
    if request.user.is_authenticated:
        if request.method =="POST":
            form = BlogCommentForm(request.POST)
            if form.is_valid():
                userid = User.objects.get(pk=request.user.id)
                blog = get_object_or_404(Blog, pk=pk)
                BlogComment.objects.create(blogid=blog, authorid=userid, 
                                            blog_comment=form.cleaned_data['Blog_comment']) 
                
                comments = BlogComment.objects.filter(blogid=pk).order_by('-created_date')
                likes = BlogLike.objects.filter(BlogLikeId=pk)
                users = User.objects.all()
                comment_form = BlogCommentForm()
                if likes:
                    for like in likes:
                        if like.PostLikedBy == userid:
                            thumb = True
                else:
                    thumb = False
                
                return render(request, "blogdetail.html", {'comment_form': comment_form, 
                                'blog': blog, 'comments': comments, 'users': users, 
                                'likes': likes, 'thumb': thumb})
        else:
            blog = get_object_or_404(Blog, pk=pk)
            comments = BlogComment.objects.filter(blogid=pk).order_by('-created_date')
            likes = BlogLike.objects.filter(BlogLikeId=pk)
            userid = User.objects.get(pk=request.user.id)
            if likes:
                    for like in likes:
                        if like.BlogLikedBy == userid:
                            thumb = True
            else:
                thumb = False
                    
            users = User.objects.all()
            comment_form = BlogCommentForm()
            blog.views += 1
            blog.save()
            return render(request, "blogdetail.html", {'comment_form': comment_form, 
                            'blog':blog, 'comments': comments, 'users': users, 
                            'likes': likes, 'thumb': thumb})
    else:
        messages.success(request, "You are supposed to be logged in to see that!")
        return redirect(reverse('index'))
    
def create_or_edit_blog(request, pk=None):
    """
    Form view to support the possibility to add
    or edit blogs
    """
    blog = get_object_or_404(Blog, pk=pk) if pk else None
    if request.method =="POST":
        print("form is a post")
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        bp_form = form.save(commit=False)
        bp_form.author = User.objects.get(pk=request.user.id) 
        bp_form.save()
        return redirect(get_blogs)
    else:
        print("form is a get")
        form = BlogPostForm(instance=blog)
    return render(request, "blogpostform.html", {'form': form})
    