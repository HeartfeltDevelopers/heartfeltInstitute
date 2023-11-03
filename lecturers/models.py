from django.db import models

from classes.models import StudentClasse
from courses.models import Course
from assignments.models import Assignment


class AssignmentNotification(models.Model):
    notification_title = models.CharField(max_length=100)
    notify_class = models.ForeignKey(StudentClasse, on_delete=models.CASCADE, related_name='notifications')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title


