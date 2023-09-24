from django.contrib import admin
from .models import StudentClasse, OfflineLesson, OnlineLesson


class StudentClasseAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'class_code', 'class_type']
    search_fields = ['class_name', 'class_code']
    list_filter = ['class_type']


admin.site.register(StudentClasse, StudentClasseAdmin)


class OfflineLessonAdmin(admin.ModelAdmin):
    list_display = ['lesson_title', 'lesson_description', 'lesson_date', 'lesson_start_time', 'lesson_end_time',
                    'course_name', 'lecturer']
    search_fields = ['lesson_title']
    list_filter = ['lesson_title', 'lesson_start_time', 'lesson_end_time']


admin.site.register(OfflineLesson, OfflineLessonAdmin)


class OnlineLessonAdmin(admin.ModelAdmin):
    list_display = ['online_title', 'lesson_description', 'lesson_date', 'lesson_start_time', 'lesson_end_time',
                    'online_platform_link', 'lecturer']
    search_fields = ['online_title', 'course_name', 'online_platform_link']
    list_filter = ['online_title', 'course_name', 'lesson_start_time', 'lesson_end_time']


admin.site.register(OnlineLesson, OnlineLessonAdmin)

