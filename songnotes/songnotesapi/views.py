from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import SongnoteSerializer
from .models import Songnote

# Create your views here.
def index(request):
  return render(request, 'songnotesapi/index.html')

class SongnoteViewSet(viewsets.ModelViewSet):
  queryset = Songnote.objects.all().order_by('song_name')
  serializer_class = SongnoteSerializer

class APIOAUTHView(generics.ListAPIView):
  def get(self, request, *args, **kwargs):
    response = {
        'message': 'token works.'
    }
    return Response(response, status=200)
