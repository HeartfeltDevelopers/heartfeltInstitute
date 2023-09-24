# forms.py
from django import forms
from .models import Assignment


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'assigned_class', 'course', 'due_date']
