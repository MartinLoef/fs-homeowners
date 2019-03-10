from django.contrib import admin
from .models import Event, EventComment, EventLike, EventJoin

admin.site.register(Event)
admin.site.register(EventComment)
admin.site.register(EventLike)
admin.site.register(EventJoin)