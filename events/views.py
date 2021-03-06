from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Event, EventLike, EventComment, User, EventJoin
from .forms import EventPostForm, EventCommentForm
from django.contrib.auth.decorators import login_required

"""All views to manage the add, edit, delete, comment 
like, join functionality for Events
"""

def create_or_edit_event(request, pk=None):
    """based on the type of post the create an event
    or delete an event"""
    if request.user.is_authenticated:
        event = get_object_or_404(Event, pk=pk) if pk else None
        if event == None:
            formtype = "Add an Event"
        else:
            formtype = "Edit an Event"
        
        if request.method =="POST":
            
            form = EventPostForm(request.POST, request.FILES, instance=event)
            ep_form = form.save(commit=False)
            ep_form.author = User.objects.get(pk=request.user.id) 
            if not ep_form.event_image:
                ep_form.event_image = "images/default-event.png"
            ep_form.save()
            return redirect(get_events)
        else:
            form = EventPostForm(instance=event)
        return render(request, "eventpostform.html", {'form': form, 'formtype': formtype})
    else:
        messages.success(request, "You are supposed to be logged in to edit that!")
        return redirect(reverse('index'))
        
def get_events(request):
    """
    show eventposts.html
    with all events
    """
    if request.user.is_authenticated:
        events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, "eventposts.html", {'events': events})
    else:
        return redirect(reverse('index'))
    
def event_detail(request, pk):
    """
    request the event detail page
    post possibility for comments on the blog
    """
    if request.user.is_authenticated:
        userid = User.objects.get(pk=request.user.id)
        event = get_object_or_404(Event, pk=pk)
        users = User.objects.all()
        likes = EventLike.objects.filter(EventLikeId=pk)
        joins = EventJoin.objects.filter(EventJoinId=pk)
        jointhumb = False
        thumb = False
        if joins:
            for join in joins:
                if join.EventJoinBy == userid:
                    jointhumb = True
        else:
            jointhumb = False
        
        if likes:
            for like in likes:
                if like.EventLikedBy == userid:
                    thumb = True
        else:
            thumb = False
    
        comments = EventComment.objects.filter(eventid=pk)
        comment_form = EventCommentForm()
        event.views += 1
        event.save()
        return render(request, "eventdetail.html", {'comment_form': 
                        comment_form, 'event': event, 'comments': comments, 
                        'users': users, 'likes': likes, 'thumb': thumb, 
                        'jointhumb': jointhumb, 'joins': joins})
    else:
        return redirect(reverse('index'))

def event_comment(request, pk):
    """
    function to save a comment on
    a specific event
    """
    if request.user.is_authenticated:
        userid = User.objects.get(pk=request.user.id)
        event = get_object_or_404(Event, pk=pk)
        if request.method =="POST":
            form = EventCommentForm(request.POST)
            if form.is_valid():
                EventComment.objects.create(eventid=event, author=userid, 
                                            event_comment=form.cleaned_data['event_comment']) 
                
                return HttpResponseRedirect(reverse('event_detail', args=(pk,)))
            else:
                return redirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('event_detail', args=(pk,)))
    else:
        return redirect(reverse('index'))

def event_like(request, pk):
    """
    users can like or remove an earlier 
    given like on event
    """
    if request.user.is_authenticated:
        eventid = Event.objects.get(pk=pk)
        userid = User.objects.get(pk=request.user.id)
    
        likes = EventLike.objects.filter(EventLikeId=pk)
        if likes:
            for like in likes:
                if like.EventLikedBy == userid:
                    EventLike.objects.filter(EventLikeId=eventid, EventLikedBy=userid).delete()
                else:
                    EventLike.objects.create(EventLikeId=eventid, EventLikedBy=userid) 
        else:
            EventLike.objects.create(EventLikeId=eventid, EventLikedBy=userid)
        return HttpResponseRedirect(reverse('event_detail', args=(pk,)))
    else:
        return redirect(reverse('index'))

def event_join(request, pk):
    """
    users can join or remove an earlier 
    given join on event
    """
    if request.user.is_authenticated:
        users = User.objects.all()
        eventid = Event.objects.get(pk=pk)
        userid = User.objects.get(pk=request.user.id)
    
        joins = EventJoin.objects.filter(EventJoinId=pk)
        
        if joins:
            for join in joins:
                if join.EventJoinBy == userid:
                    EventJoin.objects.filter(EventJoinId=eventid, EventJoinBy=userid).delete()
                    Joined = False
                else:
                    EventJoin.objects.create(EventJoinId=eventid, EventJoinBy=userid) 
                    Joined = True
        else:
            EventJoin.objects.create(EventJoinId=eventid, EventJoinBy=userid)
            Joined = True
        joins = EventJoin.objects.filter(EventJoinId=pk)
        return HttpResponseRedirect(reverse('event_detail', args=(pk,)))
    else:
        messages.success(request, "You are supposed to be logged in to Join that!")
        return redirect(reverse('index'))

def delete_event(request, pk):
    """ 
    function to delete a specific
    event
    """
    if request.user.is_authenticated:
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return redirect(reverse('get_events'))
    else:
        return redirect(reverse('index'))
        
def delete_comment(request, pk):
    """
    function to delete a comment from
    a specific event
    """
    if request.user.is_authenticated:
        eventcomment = EventComment.objects.get(pk=pk)
        event = eventcomment.eventid
        eventid = event.id
        eventcomment.delete()
        return HttpResponseRedirect(reverse('event_detail', args=(eventid,)))
    else:
        return redirect(reverse('index'))