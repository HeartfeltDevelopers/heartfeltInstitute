# urls.py
from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('add/', views.add_exam, name='add_exam'),
    # Add more URL patterns as needed
]