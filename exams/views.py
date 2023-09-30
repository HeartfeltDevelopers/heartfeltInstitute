
# views.py
from django.shortcuts import render, redirect
from .forms import ExamForm
from .models import Exam, ExamQuestion, ExamChoice
from django.contrib import messages  # Import messages

def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Exam added successfully.')  # Add a success message
            # Optionally, you can perform additional actions here, like sending notifications to students.
            return redirect('exams:add_exam')  # Redirect to the same page or a success page
    else:
        form = ExamForm()
    
    return render(request, 'exams/add_exam.html', {'form': form,})



def exam_view(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    questions = ExamQuestion.objects.filter(exam=exam)
    choices = ExamChoice.objects.filter(question__in=questions)
    return render(request, 'exam_template.html', {'exam': exam, 'questions': questions, 'choices': choices})



