from django.contrib import admin
from .models import AssignmentSubmission, StudentClass


class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "student_class",
        "assignment_title",
        "assignment_file",
        "submission_date",
    ]
    search_fields = ["student", "student_class", "assignment_title"]
    list_filter = ["student_class", "submission_date"]


admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ["student", "student_class", "created_date"]


admin.site.register(StudentClass, StudentClassAdmin)
