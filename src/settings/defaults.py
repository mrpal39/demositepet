import os
import django_heroku
import raven
from decouple import config
from dj_database_url import parse as db_url
BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = ['https://demositepet.herokuapp.com',
                 'localhost',
                 '127.0.0.1']


DJANGO_APPS = (
    'bootstrap_admin',

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
    "social_django",
    'filer',
    'mptt',
)

PROJECT_APPS = ("accounts",  "pet", "cities")

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
        "DIRS": (BASE_DIR, "../templates"),
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


            ],
            "loaders": [("django.template.loaders.cached.Loader", PROJECT_TEMPLATE_LOADERS)],
        },
    }
]

BOOTSTRAP_ADMIN_SIDEBAR_MENU = False
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "users.pipeline.add_facebook_link",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)
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

CRISPY_TEMPLATE_PACK = "bootstrap4"

CITIES_DATA_LOCATION = os.path.join(BASE_DIR, "../data/cities_data")

# CITIES_DATA_LOCATION = os.path.join(BASE_DIR, "../../data/cities_data")
# etre adat aload in server


CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = ""


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}


FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler"]
AUTH_USER_MODEL = "accounts.OwnerProfile"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())