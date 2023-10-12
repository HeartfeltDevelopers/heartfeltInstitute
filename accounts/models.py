import datetime
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

# from courses.models import Course
from .utilities import (
    generate_student_id,
    generate_employee_number,
    generate_partner_number,
)
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("admin", "admin"),
        ("lecturer", "Lecturer"),
        ("student", "Student"),
        ("alumni", "Alumni"),
        ("partner", "Partner"),
    )
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="student"
    )
    country = CountryField(max_length=20)

    def __str__(self):
        return f"{self.id}"


class UserAttributes(models.Model):
    USER_GENDER = (
        ("Female", "Female"),
        ("Male", "Male"),
    )
    root = models.IntegerField()
    rootID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user_photos/", null=True, blank=True)
    date_of_birth = models.DateField(
        null=True, blank=True, default=datetime.datetime.now
    )
    gender = models.CharField(max_length=50, choices=USER_GENDER, blank=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    church_name = models.CharField(max_length=500)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    className = models.CharField(max_length=50, default="HIM-LEC-01")
    # country = CountryField()

    def __unicode__(self):
        return "UserAttributes {}".format(self.id)


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_number = models.CharField(
        max_length=20, unique=True, default=generate_employee_number()
    )
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female")],
    )
    id_number = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    degrees_earned = models.TextField()
    institutions_attended = models.TextField()
    graduation_years = models.TextField()
    teaching_experience_years = models.PositiveIntegerField()
    previous_institutions = models.TextField()
    # courses_taught = models.ManyToManyField(Course, blank=True, related_name="teaching")
    certifications = models.TextField()
    course_management = models.TextField()
    classroom_management = models.TextField()
    assessment_evaluation = models.TextField()
    student_support = models.TextField()
    research_development = models.TextField()
    administrative_tasks = models.TextField()
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=15)
    languages_spoken = models.TextField(null=True, blank=True)
    research_interests = models.TextField(null=True, blank=True)
    publications = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.employee_number}"


class Student(models.Model):
    CURRENT_CLASS = [
        ("year one", "Year One"),
        ("year two", "Year Two"),
        ("year three", "Year Three"),
        ("year four", "Year Four"),
        ("diploma one", "Diploma One"),
        ("diploma two", "Diploma Two"),
        ("certificate", "Certificate"),
    ]
    generate_id = generate_student_id()
    root = models.IntegerField()
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True, db_column="username"
    )
    student_id = models.CharField(max_length=25, default=generate_id)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    # phone_number = models.CharField(max_length=15)
    # address = models.CharField(max_length=500)
    # enrolled_courses = models.ManyToManyField('Course', related_name='enrolled_students')
    # enrolled_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)
    current_year = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    major = models.CharField(max_length=50)
    # attendance_records = models.ManyToManyField('AttendanceRecord')
    allergies = models.TextField(null=True, blank=True)
    medical_conditions = models.TextField(null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=15)
    parent_full_name = models.CharField(max_length=100)
    parent_contact_phone = models.CharField(max_length=15)
    parent_contact_email = models.EmailField()
    nationality = models.CharField(max_length=50)
    languages_spoken = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, default="Pending", null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.student_id}"

    # Add any additional fields specific to students here


class Aluminum(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # Add any additional fields specific to alumni here

    def __str__(self):
        return self.user.username


class Partner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    partner_type_choices = [
        ("money", "Money"),
        ("food", "Food"),
        ("items", "Physical Items"),
    ]
    PARTNERSHIP_BADGE = [
        ("starter", "Starter"),
        ("silver", "Silver"),
        ("gold", "Gold"),
        ("diamond", "Diamond"),
    ]

    partnership_type = models.CharField(max_length=10, choices=partner_type_choices)
    partner_id = models.CharField(max_length=25, default=generate_partner_number)
    partnership_badge = models.CharField(max_length=20, choices=PARTNERSHIP_BADGE)
    partner_joined_date = models.DateField()
    total_partnership_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    is_partnership_recurring = models.BooleanField(default=False)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ("Credit Card", "Credit Card"),
            ("Bank Transfer", "Bank Transfer"),
            ("Cash", "Cash"),
        ],
    )
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    receipt_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name_plural = "Partners"


class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} - {self.date}"

    class Meta:
        unique_together = ("student", "date")
