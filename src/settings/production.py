from .defaults import *

import os
import environ

from decouple import config

env = environ.Env()
environ.Env.read_env()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

STATIC_URL = "/static/"

# Setting static folder for site-wide files
STATICFILES_DIRS = (os.path.join(BASE_DIR, "../static"),)

# static root folder, where static files will be collected to
default_static_root = os.path.join(BASE_DIR, "../../static_root")
STATIC_ROOT = config("STATIC_ROOT", default=default_static_root)

LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]




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
}

