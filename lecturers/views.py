# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AssignmentCreationForm
from googleapiclient.discovery import build
from google.oauth2 import service_account
from accounts.views import fetch_students


def create_assignment(request):
    if request.method == "POST":
        form = AssignmentCreationForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.lecturer = (
                request.user.lecturer
            )  # Associate assignment with the logged-in lecturer
            assignment.save()
            return redirect(
                "assignment_list"
            )  # Redirect to a list of assignments or a success page
    else:
        form = AssignmentCreationForm()

    return render(request, "accounts/lecturers/create_assignment.html", {"form": form})


def allStudents(request):
    students = fetch_students()
    context = {"students": students}
    return render(request, "lecturers/allStudents.html", context)


def success(request):
    return render(request, "success.html")


def lecturers(request):
    return render(request, "lecturers.html")
