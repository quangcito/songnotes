import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
class Songnote(models.Model):
  song_name = models.CharField(max_length=200)
  song_note = models.CharField(max_length=300)
  pub_date = models.DateTimeField("date published")

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
