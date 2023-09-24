from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_title', 'lecturer', 'current_class', 'start_date', "end_date")


admin.site.register(Course, CourseAdmin)
