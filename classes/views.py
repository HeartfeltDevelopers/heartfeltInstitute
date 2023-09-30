from django.shortcuts import render, redirect
from .forms import StudentClasseCreationForm, OnlineLessonCreationForm, OfflineLessonCreationForm
from .models import StudentClasse, OnlineLesson  # You need to define your Lecture model
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
import uuid
from datetime import datetime


def create_offline_lesson(request):
    if request.method == 'POST':
        form = OfflineLessonCreationForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new offline lesson
            offline_lesson = form.save()
            # Redirect to a different page after successful form submission
            return redirect('success_page')  # Replace 'success_page' with the actual URL name

    else:
        form = OfflineLessonCreationForm()

    return render(request, 'classes/create_offline_lesson.html', {'form': form})


def create_student_classe(request):
    # if not request.user.is_authenticated or not request.user.is_lecturer:
    #     return redirect('login')  # Redirect non-lecturers to the login page

    if request.method == 'POST':
        form = StudentClasseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace 'success_page' with the actual URL name for the success page
    else:
        form = StudentClasseCreationForm()

    return render(request, 'classes/create_class.html', {'form': form})


def create_lesson(request):
    credentials_path = settings.GOOGLE_MEET_CREDENTIALS_PATH

    unique_request_id = str(uuid.uuid4())

    if request.method == 'POST':
        form = OnlineLessonCreationForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new lesson
            online_lesson = OnlineLesson(
                online_title=form.cleaned_data['online_title'],
                lesson_description=form.cleaned_data['lesson_description'],
                lesson_date=form.cleaned_data['lesson_date'],
                lesson_start_time=form.cleaned_data['lesson_start_time'],
                lesson_end_time=form.cleaned_data['lesson_end_time'],
                course_name=form.cleaned_data['course_name'],
                material_downloads=form.cleaned_data['material_downloads'],
                lecturer=form.cleaned_data['lecturer'],

            )

            converted_lesson_date = datetime.strptime(str(online_lesson.lesson_date), '%Y-%m-%d').date()
            converted_lesson_start_time = datetime.strptime(str(online_lesson.lesson_start_time), '%H:%M:%S').time()
            converted_lesson_end_time = datetime.strptime(str(online_lesson.lesson_end_time), '%H:%M:%S').time()

            start_datetime = f'{converted_lesson_date}T{converted_lesson_start_time}-00:00'
            end_datetime = f'{converted_lesson_date}T{converted_lesson_end_time}-00:00'

            online_lesson.save()

            credentials = service_account.Credentials.from_service_account_file(
                credentials_path, scopes=['https://www.googleapis.com/auth/calendar']
            )
            service = build('calendar', 'v3', credentials=credentials)

            event = {
                'summary': online_lesson.online_title,
                'description': online_lesson.lesson_description,
                'start': {
                    'dateTime': start_datetime,
                    'timeZone': 'Africa/Harare',
                },
                'end': {
                    'dateTime': end_datetime,
                    'timeZone': 'Africa/Harare',
                },
                'conferenceData': {
                    'createRequest': {
                        'requestId': unique_request_id,
                        'conferenceSolutionKey': {'type': "hangoutsMeet"},
                    },
                },
                'conferenceDataVersion': 1,
            }
            print("this is start time: ", start_datetime)
            print("this is end time: ", end_datetime)
            event = service.events().insert(calendarId='primary', body=event).execute()

            print(event)

            if event is not None:
                print('Event created: %s' % (event.get('htmlLink')))
                # print(event['hangoutLink'])
                online_lesson.online_platform_link = event.get('htmlLink')
                online_lesson.save()
            else:
                print("Error creating event")

            return redirect('home')  # Redirect to a list of lectures or another page
    else:
        form = OnlineLessonCreationForm()

    return render(request, 'classes/create_lecture.html', {'form': form})
