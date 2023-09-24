from django import forms
from .models import AssignmentSubmission


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['assignment_title', 'assignment_description', 'assignment_file']
