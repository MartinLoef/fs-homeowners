from django import forms
from .models import Event, EventComment

class EventPostForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "details", "location", "price", "scheduled_date_start", 
        "scheduled_date_end", "event_image")

class EventCommentForm(forms.Form):
    event_comment = forms.CharField(125)