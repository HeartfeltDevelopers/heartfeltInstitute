from django.urls import path
from . import views

urlpatterns = [
    path("add-program/", views.add_program, name="add_program"),
]
