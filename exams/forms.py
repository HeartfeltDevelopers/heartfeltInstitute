# forms.py
from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'start_time', 'end_time', 'description']

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

