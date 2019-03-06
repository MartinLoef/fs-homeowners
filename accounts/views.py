from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from blogs.models import Blog, BlogComment
from events.models import Event, EventComment
from django.utils import timezone

# Create your views here.
def index(request):
    """return index.html"""
    return render(request, "index.html")


@login_required

def overview(request):
    """return overview.html"""
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    upcoming_events = Event.objects.filter(scheduled_date_start__gte=timezone.now()).order_by('scheduled_date_start')[:4]
    blog_comments = BlogComment.objects.all()
    event_comments = EventComment.objects.all()
    return render(request, "overview.html", {'blogs': blogs, 'events': events,  'event_comments': event_comments, 'blog_comments': blog_comments, 'upcoming_events': upcoming_events })

    
def logout(request):
    """log user out"""
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out")
    return redirect(reverse('SignIn'))

def SignIn(request):
    """log in"""
    if request.user.is_authenticated:
        return redirect(reverse('overview'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have succesfully logged in")
                return redirect(reverse('overview'))
                # return render(request, "overview.html")
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    # auth.logout(request)
    # messages.success(request, "You have succesfully been logged out")
    return render(request, 'SignIn.html', {'login_form': login_form})

def registration(request):  
    # if request.user.is_authenticated:
    #     return redirect(reverse('index'))
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

def profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})

def accounts(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        fields = User._meta.fields
        return render(request, "accounts.html", {'users': users, 'fields': fields})
    else:
        return redirect(reverse('index'))

def user_profile(request):
    if request.user.is_authenticated:
        userid = request.user.id
        userEmail = request.user.email
        try:
            profile = get_object_or_404(UserProfile, user=request.user.id)
            # print (profile.id)
            if profile:
                # profile = get_object_or_404(UserProfile, user=request.user.id)
                print(userid, userEmail, profile.id, profile.name, profile.phonenumber, profile.profile_image)
                profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
                return render(request, 'profile.html' , {'profile': profile})

        except:
            print("user has no profile")
            # return render(request, 'profile.html')
            profile_form = UserProfileForm()
            return render(request, 'profile.html')
    else:
        # return render(request, 'profile.html', {'UserProfileForm': UserProfileForm})
        print("something went wrong")
        return render(request, 'profile.html')
        
def edit_profile(request, id):
    profile = get_object_or_404(UserProfile, pk=id)