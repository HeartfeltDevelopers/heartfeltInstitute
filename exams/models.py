from django.db import models
from courses.models import Course
from accounts.models import Student

# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
        exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
        marks = models.PositiveIntegerField()
        question_text = models.CharField(max_length=600)
        option1 = models.CharField(max_length=200)
        option2 = models.CharField(max_length=200)
        option3 = models.CharField(max_length=200)
        option4 = models.CharField(max_length=200)
        cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
        answer = models.CharField(max_length=200, choices=cat)

        def __str__(self):
            return self.question_text


class Submission(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
        submission_time = models.DateTimeField(auto_now_add=True)
        total_score = models.PositiveIntegerField(default=0)

        def __str__(self):
            return f'{self.student} - {self.exam} - {self.total_score}'


class Response(models.Model):
        submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        selected_choice = models.ForeignKey(Question, related_name='selected_choice', on_delete=models.CASCADE)
        is_correct = models.BooleanField(default=False)
        marks_obtained = models.PositiveIntegerField(default=0)

        def __str__(self):
            return f'{self.submission} - {self.question} - {self.selected_choice}'