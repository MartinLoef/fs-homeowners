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

def get_events(request):
    """eventposts.html"""
    
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "eventposts.html", {'events': events})