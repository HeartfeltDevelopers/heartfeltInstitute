from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('create_class/', views.create_class, name='create_class'),
]
