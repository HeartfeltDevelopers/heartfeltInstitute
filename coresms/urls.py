from django.urls import path
from . import views
from accounts.views import (
    student_dashboard,
    admin_dashboard,
    lecturer_dashboard,
    user_login,
)


urlpatterns = [
    path("login/", user_login, name="login"),
    path("student-dashboard", student_dashboard, name="student-dashboard"),
    path("admin-dashboard", admin_dashboard, name="admin-dashboard"),
    path("lecturer-dashboard", lecturer_dashboard, name="lecturer-dashboard"),
    # Add other URLs as needed
]
