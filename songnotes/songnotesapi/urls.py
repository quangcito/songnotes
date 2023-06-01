from django.conf.urls import include
from django.urls import include, path, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


from . import views

app_name = "songnotesapi"
router = DefaultRouter()
router.register(r'songnotes', views.SongnoteViewSet)
router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  # path('', views.index, name='index'),
  re_path(r'^', include(router.urls)),
]
