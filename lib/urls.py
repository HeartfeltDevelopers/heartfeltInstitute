from django.urls import path
from lib.views import home

urlpatterns = [
    path("", home, name="home"),
]
