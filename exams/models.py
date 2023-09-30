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
    
    
class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return self.question_text


class ExamChoice(models.Model):
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



class StudentExamSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    total_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.student} - {self.exam} - {self.total_score}'
    

class StudentExamResponse(models.Model):
    submission = models.ForeignKey(StudentExamSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(ExamChoice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.submission} - {self.question} - {self.selected_choice}'



class StudentExamSchedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    scheduled_datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.student} - {self.exam} - {self.scheduled_datetime}'

