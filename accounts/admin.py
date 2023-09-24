from django.contrib import admin
from .models import CustomUser, Student
from .models import Lecturer, Aluminum, Partner


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')

    def get_student_number(self, obj):
        return obj.student.student_id if hasattr(obj, 'student') else None

    get_student_number.short_description = 'Student Number'


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'get_first_name', 'get_last_name', 'get_email', 'get_phone', 'get_country')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_phone(self, obj):
        return obj.user.phone if hasattr(obj.user, 'phone') else None

    def get_country(self, obj):
        return obj.user.country if hasattr(obj.user, 'country') else None

    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_email.short_description = 'Email'
    get_phone.short_description = 'Phone'
    get_country.short_description = 'Country'

    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'student_id', 'user__phone', 'user__country')


class AluminumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')  # Customize the displayed fields


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'get_phone', 'get_country', 'partnership_badge',
                    'total_partnership_amount', 'partner_id')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_phone(self, obj):
        return obj.user.phone if hasattr(obj.user, 'phone') else None

    def get_country(self, obj):
        return obj.user.country if hasattr(obj.user, 'country') else None

    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_email.short_description = 'Email'
    get_phone.short_description = 'Phone'
    get_country.short_description = 'Country'

    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'student_id', 'user__phone', 'user__country')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'get_phone', 'get_country',
                    'qualification', 'employee_number')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_phone(self, obj):
        return obj.user.phone if hasattr(obj.user, 'phone') else None

    def get_country(self, obj):
        return obj.user.country if hasattr(obj.user, 'country') else None

    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_email.short_description = 'Email'
    get_phone.short_description = 'Phone'
    get_country.short_description = 'Country'

    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'student_id', 'user__phone', 'user__country')


admin.site.register(Student, StudentAdmin)
admin.site.register(Aluminum, AluminumAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'student_id')

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'user_type', 'student_id', 'first_name', 'last_name')
#     search_fields = ('username', 'email', 'student__student_id') # Add student_number for search
#
# admin.site.register(CustomUser, CustomUserAdmin)
