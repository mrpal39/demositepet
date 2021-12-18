### dev.py
from .defaults import *
### other development-specific stuff

# import os
import os

import datetime

import environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR , 'static/' ] 
STATIC_ROOT = 'static_root/'
STATIC_URL = 'static/'


MEDIA_ROOT = '../media/'

MEDIA_URL = 'media/'

STATIC_ROOT ='static/static_root/'



LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


COMPRESS_OFFLINE = True



# AWS_ACCESS_KEY_ID = 'AKIA4JMAYYZAM37WW2G4'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'pet-static'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# # Setting media configuration

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }


# AWS_STATIC_LOCATION = 'static'
# STATICFILES_STORAGE = 'src.storage_backends.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

# AWS_PUBLIC_MEDIA_LOCATION = 'media/'
# DEFAULT_FILE_STORAGE = 'src.storage_backends.PublicMediaStorage'

# AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# PRIVATE_FILE_STORAGE = 'src.storage_backends.PrivateMediaStorage'
# AWS_S3_REGION_NAME = 'ap-south-1' #change to your region
# AWS_S3_SIGNATURE_VERSION = 's3v4'

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.sqlite3',
        
    },}
#     # 'auth_db': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': 'auth_db.sqlite3',
#     # },
#     # 'primary': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME':  'primary.sqlite3',
#     # },
#     # 'replica1': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': 'replica1.sqlite3',
#     # },
#     # 'replica2': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME':  'replica2.sqlite3',
#     # },
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'auth_system',
#         'USER': 'postgres',
#         'PASSWORD': 'Rkp3009@123',



#         'HOST': 'localhost'
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'softlanceworks@gmail.com'
EMAIL_HOST_PASSWORD = 'Softlance@123'
EMAIL_USE_TLS = True
