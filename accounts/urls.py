from django.urls import path
from accounts.views import Logout
from .views import (
    admin_dashboard,
    student_dashboard,
    lecturer_dashboard,
    user_login,
    user_details,
    registration,
    registration2,
)

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", Logout, name="logout"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("student-dashboard/", student_dashboard, name="student-dashboard"),
    path("lecturers/dashboard/", lecturer_dashboard, name="lecturer_dashboard"),
    path("user-details/<str:id>/", user_details, name="user-details"),
    path("registration/", registration, name="registration"),
    path("registration-step-2/", registration2, name="registration-step-2"),
    # Add other URLs as needed
]
