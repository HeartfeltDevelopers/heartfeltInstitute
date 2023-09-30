from django.shortcuts import render, redirect
from .forms import AssignmentSubmissionForm
from django.contrib import messages
from classes.models import StudentClasse, OfflineLesson, OnlineLesson


def class_list(request):
    classes = StudentClasse.objects.all()
    offline_lessons = OfflineLesson.objects.all()
    online_lessons = OnlineLesson.objects.all().order_by('-lesson_date')[:4]

    context= {
        'classes': classes,
        'online_lessons': online_lessons,
        'offline_lessons': offline_lessons,

    }
    return render(request, 'classes/class_list.html', context)


def submit_assignment(request):
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment submitted successfully!')
            return redirect('submit_assignment')  # Redirect to the form again
    else:
        form = AssignmentSubmissionForm()

    return render(request, 'accounts/students/submit_assignment.html', {'form': form})
