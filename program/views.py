from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CoursesForm
from program.models import Program


def add_program(request):
    programs = Program.objects.all()
    form_submitted = False

    # Check if the request is POST (form submission)
    if request.method == "POST":
        form = CoursesForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            form.save()  # Save the data into the model
            form_submitted = True  # Indicate that the form was successfully submitted
            form = CoursesForm()  # Reset the form (optional)

    # For GET request or any other method
    else:
        form = CoursesForm()

    context = {
        "form_submitted": form_submitted,
        "CoursesForm": form,
        "programs": programs,
    }
    template = "program/add_program.html"

    # Render the form in the template
    return render(request, template, context)
