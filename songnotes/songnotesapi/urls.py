from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "songnotesapi"
router = routers.DefaultRouter()
router.register(r'songnotes', views.SongnoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  path('', views.index, name='index'),
  path('api-oauth', views.APIOAUTHView.as_view(), name = 'api-oauth'),
  path('api', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
