"""
URL configuration for heartfeltsms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lecturers.views import allStudents

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("lib.urls")),
    path("coresms/", include("coresms.urls")),
    path("all-students/", allStudents, name="all-students"),
    path("accounts/", include("accounts.urls")),
    path("lecturers/", include("lecturers.urls")),
    path("students/", include("students.urls")),
    path("classes/", include("classes.urls")),
    path("register", include("email_confirmation.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
