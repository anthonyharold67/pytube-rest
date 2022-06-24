from django.urls import path
from .views import youtube

urlpatterns = [
    path("api/youtube",youtube,name="youtube"),
]
