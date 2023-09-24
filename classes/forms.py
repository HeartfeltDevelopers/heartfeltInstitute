
from django import forms
from .models import StudentClasse


class StudentClasseCreationForm(forms.ModelForm):
    class Meta:
        model = StudentClasse
        fields = ['class_name', 'class_code', 'class_type', 'class_teacher', 'lesson_title', 'lesson_description',
                  'lesson_date', 'lesson_start_time', 'lesson_end_time', 'course_name', 'material_downloads']