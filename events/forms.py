from django import forms
from .models import Event, EventComment

class EventPostForm(forms.ModelForm):
    class Meta:
        model = Event
        labels = {
            'scheduled_date_start': 'scheduled date start <br /> YYYY-MM-DD HH-MM-SS',
            'scheduled_date_end': 'scheduled date end <br /> YYYY-MM-DD HH-MM-SS',
        }
        exclude = ["author", "views"]

class EventCommentForm(forms.Form):
    event_comment = forms.CharField(max_length=125, label=False)