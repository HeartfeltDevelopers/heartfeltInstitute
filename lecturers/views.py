# views.py
from django.shortcuts import render, redirect
from .forms import AssignmentCreationForm
from googleapiclient.discovery import build
from google.oauth2 import service_account
#
# credentials = service_account.Credentials.from_service_account_file(
#     'ttttt.json',
#     scopes=['https://www.googleapis.com/auth/calendar']
# )
# service = build('calendar', 'v3', credentials=credentials)


def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentCreationForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.lecturer = request.user.lecturer  # Associate assignment with the logged-in lecturer
            assignment.save()
            form = AssignmentCreationForm()
            return render(request, 'accounts/lecturers/create_assignment.html', {'form': form})
            #return redirect('assignment_list')  # Redirect to a list of assignments or a success page
    else:
        form = AssignmentCreationForm()

    return render(request, 'accounts/lecturers/create_assignment.html', {'form': form})


