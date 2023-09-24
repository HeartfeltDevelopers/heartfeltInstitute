# views.py
from django.shortcuts import render, redirect
from .forms import AssignmentCreationForm


def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentCreationForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.lecturer = request.user.lecturer  # Associate assignment with the logged-in lecturer
            assignment.save()
            return redirect('assignment_list')  # Redirect to a list of assignments or a success page
    else:
        form = AssignmentCreationForm()

    return render(request, 'accounts/lecturers/create_assignment.html', {'form': form})
