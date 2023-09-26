from django.contrib import admin
from .models import t_url


class UrlAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(t_url, UrlAdmin)