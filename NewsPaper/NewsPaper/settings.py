"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',

    'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'news.apps.NewsConfig',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

LOGIN_URL = '/login/'

ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignupForm'}

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'), 
        ],
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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

EMAIL_HOST = 'smtp.yandex.ru' # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465 # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'bulanov-rvp' # ваше имя пользователя, например если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True 

DEFAULT_FROM_EMAIL = 'bulanov-rvp@.yandex.ru'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 8,
    }
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'DEBUG': {
#             '%(asctime)s %(levelname)s %(message)s'
#         'style': '{',  
#         },
#         'WARNING': {
#             '%(asctime)s %(levelname)s %(message)s  %(pathname)s'
#         'style': '{',  
#         },
#         'ERROR': {
#             '%(asctime)s %(levelname)s %(message)s  %(pathname)s\n%(exc_info)s'
#         'style': '{',  
#         },
#         'CRITICAL': {
#             '%(asctime)s %(levelname)s %(message)s  %(pathname)s\n%(exc_info)s'
#         'style': '{',  
#         },
#         'INFO': {
#             '%(asctime)s %(levelname)s  %(module) %(message)s'
#         'style': '{',  
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },

#     },
#     'handlers': {
#         'console_debug': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'DEBUG',
#         },
#         'console_warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'WARNING',
#         },
#         'console_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'ERROR',
#         },
#         'console_critical': {
#             'level': 'CRITICAL',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'CRITICAL',
#         },
#         'file_info': {
#             'level': 'INFO',
#             'filters': ['require_debug_False'],
#             'class': 'logging.FileHandler',
#             'filename': 'general.log',
#             'formatter': 'INFO',
#         },
#         'file_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'formatter': 'ERROR',
#         },
#         'file_security': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'formatter': 'INFO',
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'WARNING',
#             'filters': ['require_debug_False'],
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console_debug', 'console_warning', 'console_error', 'console_critical',  'file_info'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.security': {
#             'handlers': ['file_security'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'file_error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.server': {
#             'handlers': ['mail_admins', 'file_error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.template': {
#             'handlers': ['file_error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.db_backends': {
#             'handlers': ['file_error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }