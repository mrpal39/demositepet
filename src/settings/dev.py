# dev.py
from .defaults import *
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

DEBUG = False
SECRET_KEY = str(os.getenv('SECRET_KEY'))
HOST = os.environ['ONLY_HOST_NAME']
mode = os.environ['ONLY_HOST_NAME']
ALLOWED_HOSTS = [ 'https://demositepet.herokuapp.com',  
                 'localhost',
                 '127.0.0.1']


if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ORIGIN_WHITELIST = [
        'https://localhost:4200',
        f'https://login.{HOST}',
        f'http://login.{HOST}',
        f'http://www.{HOST}',
        f'https://www.{HOST}',
        f'https://{HOST}',
        f'http://{HOST}',

    ]


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR, 'static/']
STATIC_URL = 'static/'


MEDIA_ROOT = 'media/'

MEDIA_URL = 'media/'

STATIC_ROOT = 'static/static_root/'


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

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
else:
    #  DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': 'server.sqlite3',
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': '5432',


        }
    }


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
