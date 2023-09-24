from django.db import models

from classes.models import StudentClasse
from courses.models import Course


class Assignment(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    assigned_class = models.ForeignKey(StudentClasse, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AssignmentNotification(models.Model):
    notification_title = models.CharField(max_length=100)
    notify_class = models.ForeignKey(StudentClasse, on_delete=models.CASCADE, related_name='notifications')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title


