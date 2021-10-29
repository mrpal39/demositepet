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
SECRET_KEY='django-insecure-3za4=9d#hdzvkci@28nub9wgq2-y@q^z(l58t&tfq7z8xanhok'

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True




LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


COMPRESS_OFFLINE = True

# Setting media configuration
MEDIA_URL = "media/"
default_media_root = os.path.join(BASE_DIR, "..static/media")
MEDIA_ROOT = config("MEDIA_ROOT", default=default_media_root)


AWS_ACCESS_KEY_ID = 'AKIA4JMAYYZAM37WW2G4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

S3DIRECT_REGION = 'ap-south-1'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../static'),
]

AWS_STORAGE_BUCKET_NAME = 'petkennelbucket'
S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


DEFAULT_FILE_STORAGE = 'src.utils.MediaStorage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")



AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}



DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.sqlite3',
        
    },
    # 'auth_db': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'auth_db.sqlite3',
    # },
    # 'primary': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME':  'primary.sqlite3',
    # },
    # 'replica1': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'replica1.sqlite3',
    # },
    # 'replica2': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME':  'replica2.sqlite3',
    # },
}

