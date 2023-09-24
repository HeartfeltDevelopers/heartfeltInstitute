from django.contrib import admin
from .models import Assignment, AssignmentNotification


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'assigned_class', 'due_date']
    # search_fields = ['student', 'student_class', 'assignment_title']
    # list_filter = ['student_class', 'submission_date']


admin.site.register(Assignment, AssignmentAdmin)


class AssignmentNotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_title', 'notify_class', 'assignment']
    # search_fields = ['student', 'student_class', 'assignment_title']
    # list_filter = ['student_class', 'submission_date']


admin.site.register(AssignmentNotification, AssignmentNotificationAdmin)
