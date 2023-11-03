# urls.py
from django.urls import path
from .views import add_exam, create_question, take_exam, start_exam

app_name = 'exams'

urlpatterns = [
    path('add/', add_exam, name='add_exam'),
    path('question/', create_question, name='create_question'),
    path('take_exam/<int:exam_id>', take_exam, name='take_exam'),
    path('start_exam/<int:exam_id>/', start_exam, name='start_exam'),
   
]