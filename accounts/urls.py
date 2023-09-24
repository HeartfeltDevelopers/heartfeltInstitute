from django.urls import path
from . import views
from .views import CustomRegistrationView, admin_dashboard, student_dashboard, lecturer_dashboard

urlpatterns = [
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('students/dashboard/', student_dashboard, name='student_dashboard'),
    path('lecturers/dashboard/', lecturer_dashboard, name='lecturer_dashboard'),
    # Add other URLs as needed 
]
