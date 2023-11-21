from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from datetime import date
import json
from classes.forms import StudentClasseCreationForm, OnlineLessonCreationForm
from classes.models import (
    StudentClasse,
    OnlineLesson,
)  # You need to define your Lecture model
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
import uuid
from datetime import datetime

from accounts.models import CustomUser, UserAttributes
from .forms import LoginForm, RegistrationForm, UserAttributesForm
from classes.forms import LessonAllocationCreationForm
from lecturers.forms import AssignmentNotificationForm
from lecturers.models import AssignmentNotification
from django.contrib.auth.views import FormView, LoginView
from .models import Student, Lecturer, Aluminum, Partner
from lib.models import t_url
from lib.utils import *
from courses.models import Course
from accounts.models import Lecturer
from classes.models import LessonAllocation


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@login_required(login_url="/coresms/login/")
def admin_dashboard(request):
    labels = []
    data = []

    url = t_url.objects.all()

    queryset = Student.objects.all()  # order_by('-population')[:5]
    for stud in queryset:
        labels.append(stud.user.username)
        data.append(queryset.all().count())

    students = CustomUser.objects.filter(Q(user_type="student")).count()
    female_count = UserAttributes.objects.filter(Q(gender="Female")).count()
    male_count = UserAttributes.objects.filter(Q(gender="Male")).count()
    all_students = Student.objects.all()
    lecturer_count = CustomUser.objects.filter(Q(user_type="lecturer")).count()

    context = {
        "students": students,
        "female_count": female_count,
        "male_count": male_count,
        "all_students": all_students,
        "lecturer_count": lecturer_count,
        "labels": labels,
        "data": data,
        "url": url,
    }
    return render(request, "accounts/admin/dashboard.html", context)


@login_required(login_url="/coresms/login/")
def user_details(request, id):
    user_loggedin = get_object_or_404(UserAttributes, rootID=request.user.id)
    student = get_object_or_404(Student, root=request.user.id)
    user = get_object_or_404(UserAttributes, rootID=id)
    courses = Course.objects.all()
    lecturer = CustomUser.objects.filter(user_type="lecturer")

    if request.method == "POST":
        form = UserAttributesForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the user's dashboard after successful form submission
            return HttpResponseRedirect(
                reverse("user-details", kwargs={"id": user.rootID})
            )

    else:
        form = UserAttributesForm(instance=user)

    if request.method == "POST":
        lesson_allocation_creation_form = LessonAllocationCreationForm(
            request.POST, request.FILES
        )
        if lesson_allocation_creation_form.is_valid():
            lesson_allocation_creation_form.save()
            # Redirect to the user's dashboard after successful form submission
            return HttpResponseRedirect(
                reverse("user-details", kwargs={"id": user.rootID})
            )

    else:
        lesson_allocation_creation_form = LessonAllocationCreationForm(instance=user)

    user_notifications, total_notifications = fetch_notifications(user.className)
    lesson_allocation, total_lesson_allocations = fetch_lessons(user.className)

    context = {
        "current_date": date.today(),
        "student_id": student.student_id,
        "user_img": user_loggedin.photo,
        "photo": user.photo,
        "church_name": user.church_name,
        "phone": user.phone,
        "address": user.address,
        "city": user.city,
        "country": user.country,
        "form": form,
        "lesson_allocation_creation_form": lesson_allocation_creation_form,
        "notification": user_notifications,
        "total_notifications": total_notifications,
        "lecturer": lecturer,
        "courses": courses,
        "lesson_allocation": lesson_allocation,
        "total_lesson_allocations": total_lesson_allocations,
    }
    template = "accounts/users/dashboard.html"
    return render(request, template, context)


@login_required(login_url="/coresms/login/")
def student_dashboard(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    # student = get_object_or_404(Student, user_id=request.user.id)
    students = Student.objects.all().count()

    context = {
        "username": user.username,
        "students": students,
    }
    template = "accounts/students/dashboard.html"
    return render(request, template, context)


@login_required(login_url="/coresms/login/")
def lecturer_dashboard(request):
    notifications = AssignmentNotification.objects.all().order_by("-id")[:5]
    students = fetch_students()

    c = connection.cursor()
    c.cursor.execute(
        """Select a.gender, count(a.id) as total
                            FROM accounts_UserAttributes a
                            INNER JOIN accounts_Student s ON s.root = a.root
                            GROUP BY a.gender
                            """
    )
    c = dictfetchall(c)

    totalFemale = c[0]["total"] if c else 0
    totalMen = c[1]["total"] if c else 0
    total_students = totalFemale + totalMen

    if request.method == "POST":
        assignment_form = AssignmentNotificationForm(request.POST, request.FILES)
        if assignment_form.is_valid():
            assignment_form.save()
            # Redirect to the user's dashboard after successful form submission
            return HttpResponseRedirect(reverse("lecturer-dashboard"))

    else:
        assignment_form = AssignmentNotificationForm()

    context = {
        "students": students,
        "total_students": total_students,
        "totalFemale": totalFemale,
        "totalMen": totalMen,
        "assignment_form": assignment_form,
        "notifications": notifications,
    }
    return render(request, "accounts/lecturers/dashboard.html", context)


def create_lesson(request):
    credentials_path = settings.GOOGLE_MEET_CREDENTIALS_PATH

    unique_request_id = str(uuid.uuid4())

    if request.method == "POST":
        form = OnlineLessonCreationForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new lesson
            online_lesson = OnlineLesson(
                online_title=form.cleaned_data["online_title"],
                lesson_description=form.cleaned_data["lesson_description"],
                lesson_date=form.cleaned_data["lesson_date"],
                lesson_start_time=form.cleaned_data["lesson_start_time"],
                lesson_end_time=form.cleaned_data["lesson_end_time"],
                course_name=form.cleaned_data["course_name"],
                material_downloads=form.cleaned_data["material_downloads"],
                lecturer=form.cleaned_data["lecturer"],
            )
            print(online_lesson.lesson_start_time, online_lesson.lesson_date)

            converted_lesson_date = datetime.strptime(
                str(online_lesson.lesson_date), "%Y-%m-%d"
            ).date()
            converted_lesson_start_time = datetime.strptime(
                str(online_lesson.lesson_start_time), "%H:%M:%S"
            ).time()
            converted_lesson_end_time = datetime.strptime(
                str(online_lesson.lesson_end_time), "%H:%M:%S"
            ).time()

            start_datetime = (
                f"{converted_lesson_date}T{converted_lesson_start_time}:00-00:00"
            )
            end_datetime = (
                f"{converted_lesson_date}T{converted_lesson_end_time}:00-00:00"
            )

            print(start_datetime, "---", end_datetime)

            online_lesson.save()

            meeting_timezone = "Africa/Harare"

            credentials = service_account.Credentials.from_service_account_file(
                credentials_path, scopes=["https://www.googleapis.com/auth/calendar"]
            )
            service = build("calendar", "v3", credentials=credentials)

            event = {
                "summary": online_lesson.online_title,
                "description": online_lesson.lesson_description,
                "start": {
                    "dateTime": "2024-05-28T09:00:00-07:00",
                    "timeZone": "America/Los_Angeles",
                },
                "end": {
                    "dateTime": "2024-05-28T12:00:00-07:00",
                    "timeZone": "America/Los_Angeles",
                },
                "conferenceData": {
                    "createRequest": {
                        "requestId": unique_request_id,
                        "conferenceSolutionKey": {"type": "hangoutsMeet"},
                    },
                },
            }
            print("this is start time: ", start_datetime)
            print("this is end time: ", end_datetime)
            event = service.events().insert(calendarId="primary", body=event).execute()

            if event is not None:
                meet_link = event.get("htmlLink")
                print("Event created: %s" % (event.get("htmlLink")))
                online_lesson.online_platform_link = meet_link
                online_lesson.save()
            else:
                print("Error creating event")

            # meet_link = event['conferenceData']['entryPoints'][0]['uri']
            # online_lesson.online_platform_link = meet_link
            # online_lesson.save()

            return redirect(
                "lecturer-dashboard"
            )  # Redirect to a list of lectures or another page
    else:
        form = OnlineLessonCreationForm()

    return render(request, "classes/create_lecture.html", {"form": form})


class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_authenticated:
            if user.user_type == "admin":
                return "/coresms/admin/dashboard/"  # Customize the URL for the admin dashboard
            elif user.user_type == "lecturer":
                return "/coresms/lecturer/dashboard/"  # Customize the URL for the lecturer dashboard
            elif user.user_type == "student":
                return redirect("/")
                # student_dashboard_url = reverse("user-details", kwargs={"id": user.id})
                # return student_dashboard_url
            elif user.user_type == "alumni":
                return "/coresms/alumni/dashboard/"  # Customize the URL for the alumni dashboard

        return "/"


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                info = UserAttributes.objects.get(root=request.user.id)
                # Continue with your login logic if UserAttributes exists for the user
            except UserAttributes.DoesNotExist:
                return redirect("/accounts/registration-step-2")
            if user.user_type == "student":
                return redirect("/")
                # student_dashboard_url = reverse("user-details", kwargs={"id": user.id})
                # return redirect(student_dashboard_url)
            elif user.user_type == "lecturer":
                return redirect("/coresms/lecturer-dashboard")
            elif user.user_type == "admin":
                return redirect("/coresms/admin-dashboard")
            elif user.user_type == "alumni":
                return redirect("/coresms/alumni-dashboard")
    else:
        form = LoginForm(request)
    return render(request, "accounts/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect("registration-step-2")
    else:
        form = RegistrationForm()
    return render(request, "accounts/registration.html", {"form": form})


def registration2(request):
    if request.method == "POST":
        form = UserAttributesForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.user_type == "student":
                return redirect("/students/new-student")
            elif request.user_type == "lecturer":
                return redirect("/lecturer-dashboard")
            elif request.user_type == "admin":
                return redirect("/admin-dashboard")
            elif request.user_type == "alumni":
                return redirect("/alumni-dashboard")
    else:
        form = UserAttributesForm()
    return render(request, "accounts/registration2.html", {"form": form})


def Logout(request):
    logout(request)
    return redirect("/")
