from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AssignmentSubmissionForm, StudentForm

from django.contrib import messages


def new_student_account(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated:
                if request.user.user_type == "student":
                    student_dashboard_url = reverse(
                        "user-details", kwargs={"id": request.user.id}
                    )
                    return redirect(student_dashboard_url)
    else:
        form = StudentForm()

    context = {"form": form}

    template = "students/Register_New_Student.html"

    return render(request, template, context)


def submit_assignment(request):
    if request.method == "POST":
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment submitted successfully!")
            return redirect("submit_assignment")  # Redirect to the form again
    else:
        form = AssignmentSubmissionForm()

    return render(request, "accounts/students/submit_assignment.html", {"form": form})
