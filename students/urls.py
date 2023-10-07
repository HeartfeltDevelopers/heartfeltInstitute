from django.urls import path
from .views import submit_assignment, new_student_account

urlpatterns = [
    path("submit_assignment/", submit_assignment, name="submit_assignment"),
    path("new-student/", new_student_account, name="new-student"),
]
