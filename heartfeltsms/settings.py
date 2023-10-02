"""
Django settings for heartfeltsms project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

from django.contrib import staticfiles

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
DB_PASS = os.getenv("DB_PASS")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if DEBUG:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.241.136.85"]
else:
    ALLOWED_HOSTS = ["192.241.136.85", "localhost"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "coresms.apps.CoresmsConfig",
    "lib",
    "accounts",
    "finances",
    "library",
    "attendance",
    "classes",
    "students",
    "courses",
    "lecturers",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_countries",
    "exams",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = "heartfeltsms.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "heartfeltsms.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db5.sqlite3",
        }
    }
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql_psycopg2",
    #         "NAME": "bigboy",
    #         "USER": "db_admin",
    #         "PASSWORD": DB_PASS,
    #         "HOST": "localhost",
    #         "PORT": "",
    #     }
    # }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
# settings.py
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static", "static_dirs"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "static_dirs", "img")

MEDIA_URL = "/img/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# settings.py

AUTH_USER_MODEL = "accounts.CustomUser"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# settings.py


GOOGLE_MEET_CREDENTIALS_PATH = os.path.join(
    BASE_DIR, "credentials", "heartfelt-sms-419d0da5f9a0.json"
)
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

# Sets the ID of your site's URL.
# SITE_ID = 1
