from django.urls import path
from . import views

urlpatterns = [

    path('submit_assignment/', views.submit_assignment, name='submit_assignment'),
    # path('assignment_success/', views.assignment_success, name='assignment_success'),
]
