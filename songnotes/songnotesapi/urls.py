from django.urls import path

from . import views

app_name = "songnotesapi"
urlpatterns = [
  path('', views.index, name='index'),
]
