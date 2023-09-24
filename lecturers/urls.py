# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('create_assignment/', views.create_assignment, name='create_assignment'),
]
