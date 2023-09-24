from django.shortcuts import render, redirect
from .forms import StudentClasseCreationForm
from .models import StudentClasse  # You need to define your Lecture model
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
import uuid
from datetime import datetime
from pytz import timezone


def convert_time(time):
    return datetime.strptime(str(time), '%d %B %Y').strftime('%Y-%m-%d')


def create_lecture(request):
    credentials_path = settings.GOOGLE_MEET_CREDENTIALS_PATH

    unique_request_id = str(uuid.uuid4())

    if request.method == 'POST':
        form = StudentClasseCreationForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new lecture
            lecture = StudentClasse(
                class_name=form.cleaned_data['class_name'],
                class_code=form.cleaned_data['class_code'],
                class_type=form.cleaned_data['class_type'],
                class_teacher=form.cleaned_data['class_teacher'],
                lesson_title=form.cleaned_data['meeting_title'],
                lesson_description=form.cleaned_data['meeting_description'],
                lesson_date=form.cleaned_data['meeting_date'],
                lesson_start_time=form.cleaned_data['meeting_start_time'],
                lesson_end_time=form.cleaned_data['end_date'],
                course_name=form.cleaned_data['course_name'],
                material_downloads=form.cleaned_data['material_downloads'],
            )

            lecture.save()

            meeting_timezone = 'Africa/Harare'

            start_datetime = f'{convert_time(lecture.lesson_date)}T{convert_time(lecture.lesson_start_time)}'
            end_datetime = f'{convert_time(lecture.lesson_date)}T{convert_time(lecture.lesson_end_time)}'

            credentials = service_account.Credentials.from_service_account_file(
                credentials_path, scopes=['https://www.googleapis.com/auth/calendar']
            )
            service = build('calendar', 'v3', credentials=credentials)

            event = {
                'summary': lecture.lesson_title,
                'description': lecture.lesson_description,
                'start': {
                    'dateTime': start_datetime,
                    'timeZone': meeting_timezone,
                },
                'end': {
                    'dateTime': end_datetime,
                    'timeZone': meeting_timezone,
                },
                'conferenceData': {
                    'createRequest': {
                        'requestId': unique_request_id,
                    },
                },
            }

            event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()

            meet_link = event['conferenceData']['entryPoints'][0]['uri']
            lecture.meet_link = meet_link
            lecture.save()

            return redirect('lecture_list')  # Redirect to a list of lectures or another page
    else:
        form = StudentClasseCreationForm()

    return render(request, 'classes/create_lecture.html', {'form': form})
