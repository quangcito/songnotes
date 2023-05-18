from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongnoteSerializer
from .models import Songnote

# Create your views here.
def index(request):
  return render(request, 'songnotesapi/index.html')

class SongnoteViewSet(viewsets.ModelViewSet):
  queryset = Songnote.objects.all().order_by('song_name')
  serializer_class = SongnoteSerializer
