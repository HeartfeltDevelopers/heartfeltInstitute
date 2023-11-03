from django.shortcuts import render, redirect
from .forms import AssignmentSubmissionForm
from django.contrib import messages


# def submit_assignment(request):
#     if request.method == 'POST':
#         form = AssignmentSubmissionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('assignment_success')  # Redirect to a success page
#     else:
#         form = AssignmentSubmissionForm()
#
#     return render(request, 'accounts/students/submit_assignment.html', {'form': form})


