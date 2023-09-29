from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('create_class/', views.create_lesson, name='create_lesson'),
]
