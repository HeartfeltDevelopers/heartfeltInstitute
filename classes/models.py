from django.db import models
from accounts.models import Student, Lecturer
from courses.models import Course


class StudentClasse(models.Model):
    CLASS_TYPE_CHOICES = [
        ("online", "Online"),
        ("physical", "Physical"),
    ]
    class_name = models.CharField(max_length=50)
    class_code = models.CharField(max_length=10, unique=True)
    class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.class_name


class OnlineLesson(models.Model):
    online_title = models.CharField(max_length=255, null=True, blank=True)
    lesson_description = models.TextField(max_length=255, null=True, blank=True)
    lesson_date = models.DateField(null=True, blank=True)
    lesson_start_time = models.TimeField(null=True, blank=True)
    lesson_end_time = models.TimeField(null=True, blank=True)
    material_downloads = models.FileField(
        upload_to="class_materials/", null=True, blank=True
    )
    online_platform_link = models.URLField(max_length=200, null=True, blank=True)
    course_name = models.CharField(max_length=200, null=True, blank=True)
    lecturer = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.online_title


class OfflineLesson(models.Model):
    lesson_title = models.CharField(max_length=255, null=True, blank=True)
    lesson_description = models.TextField(max_length=255, null=True, blank=True)
    lesson_date = models.DateField(null=True, blank=True)
    lesson_start_time = models.TimeField(null=True, blank=True)
    lesson_end_time = models.TimeField(null=True, blank=True)
    material_downloads = models.FileField(
        upload_to="class_materials/", null=True, blank=True
    )
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.lesson_title


class Test(models.Model):
    title = models.CharField(max_length=100)
    course_name = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.CharField(max_length=500)
    marks = models.PositiveBigIntegerField()


class Choice(models.Model):
    question = models.CharField(max_length=500)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


class StudentTestSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    submission = models.DateTimeField(auto_now_add=True)
    total_score = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.student} - {self.test} - {self.total_score}"


class StudentResponse(models.Model):
    submission = models.ForeignKey(StudentTestSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.submission} - {self.question} - {self.selected_choice}"


class TestFeedBack(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    feedback_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.test}"


class LessonAllocation(models.Model):
    student_root = models.IntegerField()
    course = models.CharField(max_length=200, null=True, blank=True)
    lecturer = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, default="Inactive")

    def __str__(self):
        return f"{self.course} - {self.lecturer}"
