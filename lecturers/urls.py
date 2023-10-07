# urls.py
from django.urls import path
from .views import allStudents, success, create_assignment

urlpatterns = [
    path("create_assignment/", create_assignment, name="create_assignment"),
    path("success/", success, name="success"),
    path("all-students/", allStudents, name="all-students"),
]
