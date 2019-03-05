from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Event, EventLike, EventComment, User
from .forms import EventPostForm, EventCommentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_or_edit_event(request, pk=None):
    """"""
    event = get_object_or_404(Event, pk=pk) if pk else None
    if request.method =="POST":
        print("form is a post")
        
        form = EventPostForm(request.POST, request.FILES, instance=event)
        ep_form = form.save(commit=False)
        ep_form.author = User.objects.get(pk=request.user.id) 
        ep_form.save()
        return redirect(get_events)
    else:
        print("form is a get")
        form = EventPostForm(instance=event)
    return render(request, "eventpostform.html", {'form': form})

@login_required
def get_events(request):
    """eventposts.html"""
    
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "eventposts.html", {'events': events})

@login_required
def event_detail(request, pk):
    """eventdetail.html"""
    if request.method =="POST":
        form = EventCommentForm(request.POST)
        if form.is_valid():
            userid = User.objects.get(pk=request.user.id)
            event = get_object_or_404(Event, pk=pk)
            EventComment.objects.create(comment=event, author=userid, content_reaction=form.cleaned_data['content_reaction']) 
            
            reactions = EventComment.objects.filter(comment=pk)
            likes = EventLike.objects.filter(EventLikeId=pk)
            if likes:
                for like in likes:
                    if like.EventLikedBy == userid:
                        thumb = True
            else:
                thumb = False
                      
            users = User.objects.all()
            comment_form = EventCommentForm()
            return render(request, "eventdetail.html", {'comment_form': comment_form, 'event': event, 'reactions': reactions, 'users': users, 'likes': likes, 'thumb': thumb})
    else:
        userid = User.objects.get(pk=request.user.id)
        event = get_object_or_404(Event, pk=pk)
        reactions = EventComment.objects.filter(eventid=pk)
        likes = EventLike.objects.filter(EventLikeId=pk)
        if likes:
            for like in likes:
                if like.EventLikedBy == userid:
                    thumb = True
        else:
            thumb = False
        
        users = User.objects.all()
        comment_form = EventCommentForm()
        event.views += 1
        event.save()
        return render(request, "eventdetail.html", {'comment_form': comment_form, 'event': event, 'reactions': reactions, 'users': users, 'likes': likes, 'thumb': thumb})

def event_like(request, pk):
    """add likes"""
    event = get_object_or_404(Event, pk=pk)
    comments = EventComment.objects.filter(eventid=pk)
    users = User.objects.all()
    eventid = Event.objects.get(pk=pk)
    userid = User.objects.get(pk=request.user.id)
    
    likes = EventLike.objects.filter(EventLikeId=pk)
    comment_form = EventCommentForm()
    
    if likes:
        for like in likes:
            if like.EventLikedBy == userid:
                EventLike.objects.filter(EventLikeId=eventid, EventLikedBy=userid).delete()
                thumb = False
            else:
                EventLike.objects.create(EventLikeId=eventid, EventLikedBy=userid) 
                thumb = True
    else:
        EventLike.objects.create(EventLikeId=eventid, EventLikedBy=userid)
        thumb = True
    likes = EventLike.objects.filter(EventLikeId=pk)

    return render(request, "eventdetail.html", {'comment_form': comment_form, 'event':event, 'comments': comments, 'users': users, 'likes': likes, 'thumb': thumb })
