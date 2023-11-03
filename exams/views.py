
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExamForm, SubmissionForm
from .models import Exam, Question, Submission, Response
from students.models import Student
from .forms import QuestionForm
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



def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exams:create_question')
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }
    return render(request, 'questions/create.html', context)


def take_exam(request, exam_id):
    # Retrieve the exam and questions based on exam_id
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(exam=exam)
    
    # Calculate total possible marks and count of questions
    total_marks = sum(question.marks for question in questions)
    questions_count = questions.count()
    
    # HIM Static exam details 
    static_exam_details = {
        'start_time': exam.start_time,
        'end_time': exam.end_time,
        'course_name': exam.course.course_title,
        'total_marks': total_marks,
        'questions_count': questions_count,
    }
    
    if request.method == 'POST':
        # I will handle submission form submission logic here if needed tp start exam
        pass
    
    return render(request, 'exams/take/take_exam.html', {'exam': exam, 'static_exam_details': static_exam_details})



def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(exam=exam)
    student_profile = get_object_or_404(Student, user=request.user)
    
    if request.method == 'POST':
        form = SubmissionForm(questions, request.POST)  # Assuming you have a SubmissionForm for the submission
        if form.is_valid():
            submission = form
            
            for question in questions:
                selected_choice = form.cleaned_data.get(f'question_{question.id}')  # Adjust field name as needed
                is_correct = selected_choice == question.answer
                marks_obtained = question.marks if is_correct else 0
                
                response = Response.objects.create(
                    submission=submission,
                    question=question,
                    selected_choice=selected_choice,
                    is_correct=is_correct,
                    marks_obtained=marks_obtained
                )
                
            submission.total_score = sum(response.marks_obtained for response in submission.response_set.all())
            submission.save()
            
            answered_questions = submission.response_set.all()  # Get all answered questions for this submission
            return render(request, 'exams/take/exam_result.html', {
                'submission': submission,
                'answered_questions': answered_questions,
                'student_profile': student_profile,
            })
    else:
        form = SubmissionForm(questions, request.POST)  # Assuming you have a SubmissionForm for the submission

    return render(request, 'exams/take/start_exam.html', {
        'form': form,
        'questions': questions,
        'exam': exam,
    })
