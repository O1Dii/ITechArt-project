"""
Django settings for itechart_project project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse_lazy

import dj_database_url
import django_heroku

from .utils import _get_env_variable

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-+r7^gi8qtvv5lc7es6#o-gf%z2a#0n70uny5zh3&2=$)&1ig-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if _get_env_variable('DEBUG').lower() == 'false' else True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework.authtoken',
    'api_app',
    'main_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'itechart_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'staticfiles/templates')],
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

WSGI_APPLICATION = 'itechart_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': _get_env_variable('DB_NAME'),
        'USER': _get_env_variable('DB_USER'),
        'PASSWORD': _get_env_variable('DB_PASSWORD'),
        'HOST': _get_env_variable('DB_HOST'),
        'PORT': int(_get_env_variable('DB_PORT'))
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

AUTH_USER_MODEL = 'main_app.UserModel'

AUTHENTICATION_BACKENDS = ['main_app.backends.MyAuthBackend',
                           'django.contrib.auth.backends.ModelBackend']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

API_PAGES = int(_get_env_variable('API_PAGES'))

REDIS_HOST = _get_env_variable('REDIS_HOST')
REDIS_PORT = _get_env_variable('REDIS_PORT')
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

DATE_INPUT_FORMATS = ['%d.%m.%Y']

LOGIN_URL = reverse_lazy('main_app:register_page')
LOGIN_REDIRECT_URL = reverse_lazy('main_app:main_page')
LOGOUT_REDIRECT_URL = reverse_lazy('main_app:login_page')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = _get_env_variable('EMAIL_SENDER')
EMAIL_HOST_PASSWORD = _get_env_variable('EMAIL_SENDER_PASSWORD')
EMAIL_PORT = 587

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

IGDB_API_KEY = _get_env_variable('IGDB_API_KEY')
CONSUMER_TOKEN = _get_env_variable('TWITTER_CONSUMER_TOKEN')
CONSUMER_TOKEN_SECRET = _get_env_variable('TWITTER_CONSUMER_TOKEN_SECRET')
ACCESS_TOKEN = _get_env_variable('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = _get_env_variable('TWITTER_ACCESS_TOKEN_SECRET')

django_heroku.settings(locals())
