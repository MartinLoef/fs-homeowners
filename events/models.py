from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_author")
    title = models.CharField(max_length=200)
    details = models.TextField()
    location = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    event_image = models.ImageField(upload_to="images", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    scheduled_date_start = models.DateTimeField(blank=True, null=True)
    scheduled_date_end = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.title

class EventComment(models.Model):
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_comment_id")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_author_id")
    event_comment = models.CharField(max_length=125)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_reaction

class EventLike(models.Model):
    EventLikeId = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_like_id")
    EventLikedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_liked_by_user")
    
    def __int__(self):
        return "EventLikeId: {0} / EventID: {1} / User: {2}".format(
            self.id, self.EventLikeId, self.EventLikedBy)