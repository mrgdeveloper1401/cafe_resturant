"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from .db.db import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
CREATEAPP = [
    'accounts.apps.AccountsConfig',
    'core.apps.CoreConfig',
    'images.apps.ImagesConfig',
    'products.apps.ProductsConfig',
    'contact.apps.ContactConfig',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coupon_management',
    'django_render_partial',
    # 'storages',
    *CREATEAPP
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR /'static/',
]
STATIC_ROOT = '/static/'

MEDIA_URL ='media/'
MEDIA_ROOT = BASE_DIR /'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# user
AUTH_USER_MODEL = 'accounts.User'


# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             'AWS_ACCESS_KEY_ID': '4e60ba7e-63b9-489f-b054-a86c3bba8157',
#             'AWS_SECRET_ACCESS_KEY': 'a1aea485118bcc0d8b1c6eca09fe4fe75012d24e6cda712692976fcfe752118d',
#             'AWS_S3_ENDPOINT_URL': 's3.ir-tbz-sh1.arvanstorage.ir',
#             'AWS_STORAGE_BUCKET_NAME': 'reser-django-food',
            
             

#         },
#     }
# }


# # access key arvancloude
# AWS_ACCESS_KEY_ID = '4e60ba7e-63b9-489f-b054-a86c3bba8157'

# # secret key arvancloude
# AWS_SECRET_ACCESS_KEY = 'a1aea485118bcc0d8b1c6eca09fe4fe75012d24e6cda712692976fcfe752118d'

# # endpoint url
# AWS_S3_ENDPOINT_URL = 's3.ir-tbz-sh1.arvanstorage.ir'

# # bucket name
# AWS_STORAGE_BUCKET_NAME = 'reser-django-food'

# # service name
# AWS_SERVICE_NAME = 's3'

# # Replace similar files
# AWS_S3_FILE_OVERWRITE = False

# # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STORAGES = {}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vtccewsfulkaotuo'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'e-commers shop'

# change expride data session
# SESSION_COOKIE_AGE = 10000000000