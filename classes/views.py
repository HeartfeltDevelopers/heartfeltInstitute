from django.shortcuts import render, redirect
from .forms import StudentClasseCreationForm, OnlineLessonCreationForm
from .models import StudentClasse, OnlineLesson  # You need to define your Lecture model
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
from django.contrib import messages
import uuid
from datetime import datetime


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

            print(event)

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

            return redirect("success")  # Redirect to a list of lectures or another page
    else:
        form = OnlineLessonCreationForm()

    return render(request, "classes/create_lecture.html", {"form": form})


def AllOnlineClasses(request):
    online_lessons = OnlineLesson.objects.all().order_by("-id")[:20]

    context = {
        "online_lessons": online_lessons,
    }

    template = "classes/allOnlineLessons.html"

    return render(request, template, context)
