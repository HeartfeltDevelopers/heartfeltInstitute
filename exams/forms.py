# forms.py
from django import forms
from .models import Exam
from .models import Question



class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'start_time', 'end_time', 'description']

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['exam', 'marks', 'question_text', 'option1', 'option2', 'option3', 'option4', 'answer']

        widgets = {
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'marks': forms.TextInput(attrs={'class': 'form-control'}),
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'option1': forms.TextInput(attrs={'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'class': 'form-control'}),
            'option4': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Select(attrs={'class': 'form-control'}),
        }

class SubmissionForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        for question in questions:
            # Dynamically generate field names based on question IDs
            field_name = f'question_{question.id}'
            choices = [
                (f'Option{i}', getattr(question, f'option{i}')) for i in range(1, 5)
            ]  # Assuming option1, option2, ..., option4 are the question options
            self.fields[field_name] = forms.ChoiceField(
                label=question.question_text,
                choices=choices,
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
            )