from django import forms
from .models import Event, EventComment

class EventPostForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ["author", "views"]

class EventCommentForm(forms.Form):
    event_comment = forms.CharField(max_length=125, label=False)