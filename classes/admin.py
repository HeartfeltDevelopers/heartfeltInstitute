from django.contrib import admin
from .models import StudentClasse


class StudentClasseAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'class_code', 'class_type', 'class_teacher', 'start_date', 'end_date',
                    'online_platform', 'description', 'duration']
    search_fields = ['class_name', 'class_code']
    list_filter = ['class_type', 'start_date', 'end_date']


admin.site.register(StudentClasse, StudentClasseAdmin)
