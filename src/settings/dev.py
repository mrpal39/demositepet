### dev.py
from .defaults import *
### other development-specific stuff

# 
import os
import django_heroku

import environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
# SECRET_KEY=django-insecure-3za4=9d#hdzvkci@28nub9wgq2-y@q^z(l58t&tfq7z8xanhok

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG =  env('DEBUG')



STATIC_URL = "/static/"

# Setting static folder for site-wide files
STATICFILES_DIRS = (os.path.join(BASE_DIR, "../static"),)

# static root folder, where static files will be collected to
default_static_root = os.path.join(BASE_DIR, "../../static_root")
STATIC_ROOT = config("STATIC_ROOT", default=default_static_root)

LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


COMPRESS_OFFLINE = True

# Setting media configuration
MEDIA_URL = "/media/"
default_media_root = os.path.join(BASE_DIR, "../../media")
MEDIA_ROOT = config("MEDIA_ROOT", default=default_media_root)
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

# DATABASE_ROUTERS = ['routers.routing.AuthRouter',
#                     'routers.routing.PrimaryReplicaRouter']
django_heroku.settings(locals())
