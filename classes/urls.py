from django.urls import path
from . import views
from .views import create_student_classe

urlpatterns = [

    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('create_class/', create_student_classe, name='create_student_classe'),
    path('create_offline_lesson/', views.create_offline_lesson, name='create_offline_lesson'),

]
