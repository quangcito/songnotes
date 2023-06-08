from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import SongnoteSerializer
from .models import Songnote
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User
from songnotesapi.models import Songnote
from songnotesapi.serializers import SongnoteSerializer, UserSerializer
from songnotesapi.permissions import IsOwnerOrReadOnly

# Create your views here.
def index(request):
  return render(request, 'songnotesapi/index.html')

class SongnoteViewSet(viewsets.ModelViewSet):
  queryset = Songnote.objects.all().order_by('song_name')
  serializer_class = SongnoteSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  This viewset automatically provide `list` and `retrieve` action.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

