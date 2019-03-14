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
        blogid = Blog.objects.get(pk=pk)
        userid = User.objects.get(pk=request.user.id)
        likes = BlogLike.objects.filter(BlogLikeId=pk)
        
        if likes:
            for like in likes:
                if like.BlogLikedBy == userid:
                    BlogLike.objects.filter(BlogLikeId=blogid, 
                                            BlogLikedBy=userid).delete()
                else:
                    BlogLike.objects.create(BlogLikeId=blogid, 
                                            BlogLikedBy=userid) 
        else:
            BlogLike.objects.create(BlogLikeId=blogid, BlogLikedBy=userid)

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
        userid = User.objects.get(pk=request.user.id)
        blog = get_object_or_404(Blog, pk=pk)
        comments = BlogComment.objects.filter(blogid=pk).order_by('-created_date')
        likes = BlogLike.objects.filter(BlogLikeId=pk)
        if likes:
            for like in likes:
                if like.BlogLikedBy == userid:
                    thumb = True
                else:
                    thumb = False
        else:
            thumb = False
            
        users = User.objects.all()
        comment_form = BlogCommentForm()
        blog.views += 1
        blog.save()        
        return render(request, "blogdetail.html", {'comment_form': comment_form, 
                    'blog': blog, 'comments': comments, 'users': users, 
                    'likes': likes, 'thumb': thumb})
        
    else:
        messages.success(request, "You are supposed to be logged in to see that!")
        return redirect(reverse('index'))

def blogpost_comment(request, pk):
    userid = User.objects.get(pk=request.user.id)
    if request.method =="POST":
        form = BlogCommentForm(request.POST)
        print(form)
        if form.is_valid():
            userid = User.objects.get(pk=request.user.id)
            blog = get_object_or_404(Blog, pk=pk)
            BlogComment.objects.create(blogid=blog, authorid=userid, 
                                        blog_comment=form.cleaned_data['Blog_comment'])
            return HttpResponseRedirect(reverse('blog_detail', args=(pk,)))
        else:
            return HttpResponseRedirect(reverse('blog_detail', args=(pk,)))
    else:
        return HttpResponseRedirect(reverse('blog_detail', args=(pk,)))
    
def create_or_edit_blog(request, pk=None):
    """
    Form view to support the possibility to add
    or edit blogs
    """
    
    blog = get_object_or_404(Blog, pk=pk) if pk else None
    if blog == None:
        formtype = "Add a Blog"
    else:
        formtype = "Edit a Blog"
        
    if request.method =="POST":

        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        bp_form = form.save(commit=False)
        bp_form.author = User.objects.get(pk=request.user.id) 
        bp_form.save()
        return redirect(get_blogs)
    else:

        form = BlogPostForm(instance=blog)
        
    return render(request, "blogpostform.html", {'form': form, 'formtype': formtype})

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect(reverse('get_blogs'))

def delete_blog_comment(request, pk):
    blogcomment = BlogComment.objects.get(pk=pk)
    blog = blogcomment.blogid
    blogid = blog.id
    blogcomment.delete()
    return HttpResponseRedirect(reverse('blog_detail', args=(blogid,)))
    