from django.urls import path
from accounts.views import Logout
from .views import (
    CustomRegistrationView,
    admin_dashboard,
    student_dashboard,
    lecturer_dashboard,
    user_login,
    user_details,
)

urlpatterns = [
    path("register/", CustomRegistrationView.as_view(), name="register"),
    path("login/", user_login, name="login"),
    path("logout/", Logout, name="logout"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("student-dashboard/", student_dashboard, name="student-dashboard"),
    path("lecturers/dashboard/", lecturer_dashboard, name="lecturer_dashboard"),
    path("user-details/<str:id>/", user_details, name="user-details"),
    # Add other URLs as needed
]
