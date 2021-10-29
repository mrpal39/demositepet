### dev.py
from .defaults import *
### other development-specific stuff

# import os
import os



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

DEBUG = False




# static root folder, where static files will be collected to
default_static_root = os.path.join(BASE_DIR, "../../static_root")
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


COMPRESS_OFFLINE = True

# Setting media configuration
MEDIA_URL = "/media/"
default_media_root = os.path.join(BASE_DIR, "../media")
MEDIA_ROOT = config("MEDIA_ROOT", default=default_media_root)


AWS_ACCESS_KEY_ID = 'AKIA4JMAYYZAM37WW2G4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'petkennelbucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../static'),
]


STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'







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

