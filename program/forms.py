from django import forms
from .models import ProgramLevel, Program, Courses


class ProgramLevelForm(forms.ModelForm):
    class Meta:
        model = ProgramLevel
        fields = ["level_name"]


class ProgramForm(forms.ModelForm):
    program_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Program name",
            }
        ),
        label="",
    )

    class Meta:
        model = Program
        fields = ["program_name", "level"]


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ["course_name", "program", "level", "student_id"]
