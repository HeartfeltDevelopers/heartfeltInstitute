from django import forms
from .models import AssignmentSubmission
from accounts.models import Student


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ["assignment_title", "assignment_description", "assignment_file"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["root", "user", "student_id", "status"]
