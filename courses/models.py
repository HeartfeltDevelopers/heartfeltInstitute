from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser, Aluminum, Lecturer, Student  # , Semester
from django.conf import settings
from .validators import ASCIIUsernameValidator

A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
PASS = "PASS"
FAIL = "FAIL"

GRADE = (
    (A, 'A'),
    (B, 'B'),
    (C, 'C'),
    (D, 'D'),
    (F, 'F'),
)

COMMENT = (
    (PASS, "PASS"),
    (FAIL, "FAIL"),
)

CURRENT_CLASS = (
    ('first_year', 'first_year'),
    ('second_year', 'second_year'),
    ('third_year', 'third_year'),
    ('certificate', 'certificate'),
    ('diploma_one', 'diploma_one'),
    ('diploma_two', 'diploma_two'),
)

FIRST = "First"
SECOND = "Second"

SEMESTER = (
    (FIRST, "First"),
    (SECOND, "Second"),
)


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Course(models.Model):
    LOCATION = [
        ('online', 'Online'),
        ('institute', 'Institute'),
        ('hybrid', 'Hybrid')
    ]
    course_code = models.CharField(max_length=10, unique=True)
    course_title = models.CharField(max_length=200)
    description = models.TextField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, db_column='user.last_name')
    start_date = models.DateField()
    end_date = models.DateField()
    #max_students = models.PositiveIntegerField()
    credits = models.PositiveIntegerField()
    course_unit = models.CharField(max_length=200)
    current_class = models.CharField(choices=CURRENT_CLASS, max_length=30, blank=True)
    semester = models.CharField(choices=SEMESTER, max_length=20)
    is_elective = models.BooleanField(default=False, blank=True, null=True)
    location = models.CharField(max_length=25, choices=LOCATION)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': self.pk})


class TakenCourse(models.Model):
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='taken_courses')
    ca = models.PositiveIntegerField(blank=True, null=True, default=0)
    exam = models.PositiveIntegerField(blank=True, null=True, default=0)
    total = models.PositiveIntegerField(blank=True, null=True, default=0)
    grade = models.CharField(choices=GRADE, max_length=1, blank=True)
    comment = models.CharField(choices=COMMENT, max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('update_score', kwargs={'pk': self.pk})

    def get_total(self, ca, exam):
        return int(ca) + int(exam)

    def get_grade(self, ca, exam):
        total = int(ca) + int(exam)
        if total >= 70:
            grade = A
        elif total >= 60:
            grade = B
        elif total >= 50:
            grade = C
        elif total >= 45:
            grade = D
        else:
            grade = F
        return grade

    def get_comment(self, grade):
        if not grade == "F":
            comment = PASS
        else:
            comment = FAIL
        return comment

    # def carry_over(self, grade):
    #     if grade == F:
    #         CarryOverStudent.objects.get_or_create(student=self.student, course=self.course)
    #     else:
    #         CarryOverStudent.objects.get(student=self.student, course=self.course).delete()


class CourseAllocation(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, db_column='last_name')
    courses = models.ManyToManyField(Course, related_name='allocated_course')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.lecturer.user.username


class CarryOverStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100, choices=SEMESTER, blank=True, null=True)
    # session = models.CharField(max_length=100, blank=True, null=True)
    current_class = models.CharField(choices=CURRENT_CLASS, max_length=30, blank=True, null=True)

    def __str__(self):
        return self.student.student_id


class RepeatingStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_class = models.CharField(max_length=100, choices=CURRENT_CLASS)
    session = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.student.student_id


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.CharField(max_length=20, choices=COMMENT)
    semester = models.CharField(max_length=100, choices=SEMESTER)
    session = models.CharField(max_length=100, blank=True, null=True)
    current_class = models.CharField(max_length=100, choices=CURRENT_CLASS)
