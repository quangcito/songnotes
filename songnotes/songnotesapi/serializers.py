from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Songnote

class SongnoteSerializer(serializers.HyperlinkedModelSerializer):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Songnote
    fields = ('url', 'id', 'owner', 'song_name', 'song_note')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    songnotes = serializers.HyperlinkedRelatedField(many=True, view_name='songnote-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="songnotesapi:user-detail")


    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'songnotes']
