# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-21 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('scheduled_date_start', models.DateTimeField(blank=True, null=True)),
                ('scheduled_date_end', models.DateTimeField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_comment', models.CharField(max_length=125)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_author_id', to=settings.AUTH_USER_MODEL)),
                ('eventid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_comment_id', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventLikeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_like_id', to='events.Event')),
                ('EventLikedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_liked_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]