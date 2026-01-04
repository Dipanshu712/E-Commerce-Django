# from pathlib import Path
# import os
# from django.contrib.messages import constants as message_constants
# from dotenv import load_dotenv

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-w-rh898&6e_oe&71*n$m4i)o8+3^lw#&=lbqvbs)4vebhw%kbn'
# DEBUG = False
# ALLOWED_HOSTS = []

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'ecommerceapp',
#     'authcart',
#     'django.contrib.humanize',

# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'ecommerce.urls'

# # Match template directory exactly to folder on disk (default: lowercase)
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, "templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'ecommerce.wsgi.application'

# # Load .env early so DATABASES can pick up credentials from it during local runs
# load_dotenv()

# # Configure DATABASES: prefer Postgres when full credentials are present, otherwise
# # fall back to a local SQLite database for easy local development.
# PG_NAME = os.getenv('PGDATABASE')
# PG_USER = os.getenv('PGUSER')
# PG_PASSWORD = os.getenv('PGPASSWORD')
# PG_HOST = os.getenv('PGHOST')
# PG_PORT = os.getenv('PGPORT')

# if PG_NAME and PG_USER and PG_PASSWORD:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': PG_NAME,
#             'USER': PG_USER,
#             'PASSWORD': PG_PASSWORD,
#             'HOST': PG_HOST or 'localhost',
#             'PORT': PG_PORT or '5432',
#         }
#     }
# else:
#     # Fall back to SQLite for local development when Postgres isn't configured.
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': str(BASE_DIR / 'db.sqlite3'),
#         }
#     }

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # FOR Media URL 
# import os

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Email setup (example for Gmail)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'mdipanshu713@gmail.com'
# EMAIL_HOST_PASSWORD = 'qqfa ixxl uefl chuj'  # App Password
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# # Enable Bootstrap-friendly message tags
# MESSAGE_TAGS = {
#     message_constants.ERROR: 'danger',
#     message_constants.WARNING: 'warning',
#     message_constants.SUCCESS: 'success',
#     message_constants.INFO: 'info',
# }


# RAZORPAY_KEY_ID = 'rzp_test_Rd8ipY3kMs5yKY'
# RAZORPAY_KEY_SECRET = 'rc1p9poX4vO9K30vxCGtcKWI'

# ALLOWED_HOSTS = [
#     'giithubb-production.up.railway.app',
#     'localhost',
#     '127.0.0.1'
# ]

# SECRET_KEY = os.getenv('SECRET_KEY')
# DEBUG = os.getenv('DEBUG', 'False') == 'True'

# # Use os.getenv(...) for other sensitive or environment-specific settings



from pathlib import Path
import os
from django.contrib.messages import constants as message_constants

# ---------------------------------------------------------
# Base Directory
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------
# Security (LOCAL)
# ---------------------------------------------------------
SECRET_KEY = 'django-insecure-w-rh898&6e_oe&71*n$m4i)o8+3^lw#&=lbqvbs)4vebhw%kbn'
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# ---------------------------------------------------------
# Installed Apps
# ---------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ecommerceapp',
    'authcart',

    'django.contrib.humanize',
]

# ---------------------------------------------------------
# Middleware
# ---------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

# ---------------------------------------------------------
# Templates
# ---------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# ---------------------------------------------------------
# Local SQLite Database
# ---------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------------------------------------------
# Password Validation
# ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------------
# Internationalization
# ---------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# Static Files
# ---------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------------------------------------------------
# Media Files
# ---------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------------------------------------------------
# Default Primary Key Type
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------------------------------------
# Email (Local Gmail SMTP)
# ---------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mdipanshu713@gmail.com'
EMAIL_HOST_PASSWORD = 'zbkl ebzy hwoe jepd'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ---------------------------------------------------------
# Django Message Tags (Bootstrap)
# ---------------------------------------------------------
MESSAGE_TAGS = {
    message_constants.ERROR: 'danger',
    message_constants.WARNING: 'warning',
    message_constants.SUCCESS: 'success',
    message_constants.INFO: 'info',
}

# ---------------------------------------------------------
# Razorpay Test Keys (Local Only)
# ---------------------------------------------------------
RAZORPAY_KEY_ID = 'rzp_test_Rd8ipY3kMs5yKY'
RAZORPAY_KEY_SECRET = 'rc1p9poX4vO9K30vxCGtcKWI'


