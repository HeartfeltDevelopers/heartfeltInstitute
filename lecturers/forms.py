# forms.py
from django import forms
from assignments.models import Assignment


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'assigned_class', 'course', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }