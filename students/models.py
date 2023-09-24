from django.db import models
from accounts.models import Student, Lecturer
from classes.models import StudentClasse
from courses.models import Course


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    lecturer_name = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
    student_class = models.ForeignKey(StudentClasse, on_delete=models.SET_NULL, null=True)
    assignment_title = models.CharField(max_length=250)
    assignment_description = models.TextField(max_length=200)
    assignment_file = models.FileField(upload_to='assignment_submissions')
    submission_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student}, {self.student_class}, {self.assignment_file}, {self.assignment_title}, {self.submission_date}'


class SportsActivity(models.Model):
    activity_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    max_participants = models.PositiveIntegerField()

    def __str__(self):
        return self.activity_name


class Club(models.Model):
    club_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.club_name


