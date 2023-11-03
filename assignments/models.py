from django.db import models
from courses.models import Course
from classes.models import StudentClasse
from courses.models import Course
from accounts.models import Lecturer, Student


#class Lecturer(models.Model):
   # name = models.CharField(max_length=255)
  #  email = models.EmailField()

class Assignment(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    assigned_class = models.ForeignKey(StudentClasse, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClasse, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to='submissions/')

