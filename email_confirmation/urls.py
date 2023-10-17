from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
]
