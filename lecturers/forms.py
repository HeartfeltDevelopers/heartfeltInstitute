# forms.py
from django import forms
from .models import Assignment, AssignmentNotification


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "description", "assigned_class", "course", "due_date"]


class AssignmentNotificationForm(forms.ModelForm):
    class Meta:
        model = AssignmentNotification
        fields = ["notification_title", "notify_class", "message", "assignment"]
