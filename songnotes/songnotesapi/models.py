import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Songnote(models.Model):
  song_name = models.CharField(max_length=200)
  song_note = models.CharField(max_length=300)
  pub_date = models.DateTimeField("date published")
  owner = models.ForeignKey('auth.User', related_name='songnotes', on_delete=models.CASCADE)


  def __str__(self) -> str:
    return self.song_name

  @admin.display(
    boolean=True,
    ordering="pub_date",
    description="Published recently?",
  )

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
