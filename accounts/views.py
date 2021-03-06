from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils import timezone
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from blogs.models import Blog, BlogComment
from events.models import Event, EventComment


# Create your views here.
def index(request):
    """return index.html if user is not in session
    if in session show overview page"""
    if request.user.is_authenticated:
        return redirect(reverse('overview'))
    else:
        return render(request, "index.html")

def overview(request):
    """return overview.html
    show latest blog, newest events
    and upcoming next 5 events
    """
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
        events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
        upcoming_events = Event.objects.filter(scheduled_date_start__gte=timezone.now()).order_by('scheduled_date_start')[:4]
        blog_comments = BlogComment.objects.all()
        event_comments = EventComment.objects.all()
        return render(request, "overview.html", {'blogs': blogs, 'events': events,  
                    'event_comments': event_comments, 'blog_comments': blog_comments, 
                    'upcoming_events': upcoming_events })
    else:
        return redirect(reverse('index'))

def logout(request):
    """log user out"""
    auth.logout(request)
    messages.error(request, "You have succesfully been logged out")
    return redirect(reverse('index'))

def SignIn(request):
    """log in"""
    if request.user.is_authenticated:
        return redirect(reverse('overview'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        username=request.POST['username']
        user = User.objects.get(username=username)
        if user.is_active:
            
            if login_form.is_valid():
                user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
                if user:
                    auth.login(user=user, request=request)
                    messages.success(request, "You have succesfully logged in")
                    return redirect(reverse('overview'))
    
                else:
                    login_form.add_error(None, "Your username or password is incorrect")
        else:
            login_form.add_error(None, "Your username is suspended")
    else:
        login_form = UserLoginForm()

    return render(request, 'SignIn.html', {'login_form': login_form})

def registration(request):  
    """
    form to register en new user to the site, 
    can only be done by an administrator
    """
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == "POST":
                register_form = UserRegistrationForm(request.POST)
                if register_form.is_valid():
                    user = register_form.save(commit=False)
                    user.is_active = True
                    user.save()
                    current_site = get_current_site(request)
                    message = render_to_string('signup.html', {
                        'user':user, 
                        'domain':current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    mail_subject = 'We have created an new Commonhold account for you, please activate'
                    to_email = register_form.cleaned_data.get('email')
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return redirect(reverse('accounts'))
            else:
                register_form = UserRegistrationForm()
            return render(request, 'registration.html', 
                    {'register_form': register_form})
        else:
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def accounts(request):
    """
    show all acounts from the database
    exclude the admin account
    """
    if request.user.is_authenticated:
        users = User.objects.exclude(pk=1)
        fields = User._meta.fields
        return render(request, "accounts.html", {'users': users, 'fields': fields})
    else:
        return redirect(reverse('index'))

def user_suspend(request, pk):
    """
    function to suspend a user_activate
    makes in impossible to login
    """
    if request.user.is_authenticated:
        if request.user.is_staff:
            userid = User.objects.get(pk=pk)
            if userid:
                userid.is_active = False
                userid.save()
                messages.success(request, "You suspended the account!")
                return HttpResponseRedirect(reverse('accounts'))
        else:
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def user_activate(request, pk):
    """
    reactivate an suspended user
    """
    if request.user.is_authenticated:
        if request.user.is_staff:
            userid = User.objects.get(pk=pk)
            if userid:
                userid.is_active = True
                userid.save()
                messages.success(request, "You Activated the account!")
                return HttpResponseRedirect(reverse('accounts'))
        else:
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))