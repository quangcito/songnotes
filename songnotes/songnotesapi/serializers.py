from rest_framework import serializers

from .models import Songnote

class SongnoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Songnote
    fields = ('id', 'song_name', 'song_note')
