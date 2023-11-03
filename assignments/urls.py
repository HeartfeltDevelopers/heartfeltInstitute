from django.urls import path
from . import views

urlpatterns = [
    path('assignment-form/', views.assignment_form, name='assigmnent_form'),
]
