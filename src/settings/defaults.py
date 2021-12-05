import os
import django_heroku
import raven

SECRET_KEY='django-insecure-3za4=9d#hdzvkci@28nub9wgq2-y@q^z(l58t&tfq7z8xanhok'

from datetime import timedelta

from decouple import config
from dj_database_url import parse as db_url
BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = ['https://demositepet.herokuapp.com',
                 'localhost',
                 '127.0.0.1']


DJANGO_APPS = (

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
)

THIRD_PARTS_APPS = (
    "compressor",
    "corsheaders",
    "crispy_forms",
    "easy_thumbnails",
    "raven.contrib.django.raven_compat",
    "password_reset",
    "rest_framework",
    'rest_framework_simplejwt',
    'djoser',
    
    "social_django",
    'filer',
    
    
    
    'mptt',
    
    
    
    
    'allauth',
    'allauth.account',
    'storages',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

)

PROJECT_APPS = ("accounts",  "pet", "cities","common",'kennels')

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTS_APPS
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
FILER_CANONICAL_URL = 'sharing/'

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# templates


PROJECT_TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (BASE_DIR, "templates"),
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'django.template.context_processors.request',
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",

                "common.context_processors.us_pet",

            ],
            "loaders": [("django.template.loaders.cached.Loader", PROJECT_TEMPLATE_LOADERS)],
        },
    }
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
WSGI_APPLICATION = 'src.wsgi.application'
ROOT_URLCONF = 'src.urls'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


THUMBNAIL_ALIASES = {
    "": {
        "pet_thumb": {"size": (350, 350), "crop": True, "upscale": True},
        "pet_poster": {"size": (550, 550), "crop": True, "upscale": True},
    }
}


THUMBNAIL_BASEDIR = "pet_thumbs"

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = '/profiles/'

CRISPY_TEMPLATE_PACK = "bootstrap4"

CITIES_DATA_LOCATION = os.path.join(BASE_DIR, "../data/cities_data")

# CITIES_DATA_LOCATION = os.path.join(BASE_DIR, "../../data/cities_data")
# etre adat aload in server


CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = ""




FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler"]
AUTH_USER_MODEL = "accounts.OwnerProfile"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.TokenAuthentication',

        "rest_framework.authentication.SessionAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
  
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
DJOSER = {
    "LOGIN_FIELD":"email",
    'USER_CREATE_PASSWORD_RETYPE':True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION":True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION":True,
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SET_USERNAME_RETYPE':True,
    'SET_PASSWORD_RETYPE':True,
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create':'accounts.serializers.UserCreateSerializer',
        'user':'accounts.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer',

        
        },
}

django_heroku.settings(locals())