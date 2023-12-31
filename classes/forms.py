from django import forms
from .models import StudentClasse, OnlineLesson, OfflineLesson, LessonAllocation


class StudentClasseCreationForm(forms.ModelForm):
    class Meta:
        model = StudentClasse
        fields = ["class_name", "class_code", "class_type"]


class OnlineLessonCreationForm(forms.ModelForm):
    lesson_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    lesson_start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    lesson_end_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = OnlineLesson
        fields = [
            "online_title",
            "lesson_description",
            "lesson_date",
            "lesson_start_time",
            "lesson_end_time",
            "material_downloads",
            "course_name",
            "lecturer",
        ]

        # widgets = {

        # 'lesson_date': forms.DateInput(attrs={'type': 'date'}),
        # 'lesson_start_time': forms.TimeInput(attrs={'type': 'time'}),
        # 'lesson_end_time': forms.TimeInput(attrs={'type': 'time'}),

        #
        # }


class OfflineLessonCreationForm(forms.ModelForm):
    class Meta:
        model = OfflineLesson
        fields = [
            "lesson_title",
            "lesson_description",
            "lesson_date",
            "lesson_start_time",
            "lesson_end_time",
            "material_downloads",
            "course_name",
            "lecturer",
        ]

        widgets = {
            "lesson_date": forms.DateInput(attrs={"type": "date"}),
            "lesson_start_time": forms.TimeInput(attrs={"type": "time"}),
            "lesson_end_time": forms.TimeInput(attrs={"type": "time"}),
        }


class LessonAllocationCreationForm(forms.ModelForm):
    class Meta:
        model = LessonAllocation
        fields = ["student_root", "course", "lecturer"]
