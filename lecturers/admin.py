from django.contrib import admin
from .models import AssignmentNotification


class AssignmentNotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_title', 'notify_class', 'assignment']
    # search_fields = ['student', 'student_class', 'assignment_title']
    # list_filter = ['student_class', 'submission_date']


admin.site.register(AssignmentNotification, AssignmentNotificationAdmin)
