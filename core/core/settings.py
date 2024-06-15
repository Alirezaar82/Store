"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY",default='django-insecure-hp@qbs6wb@kf1)8cdunki=j#3zzjrk7^34c!xwxvt&w6+498#v')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG",cast=bool,default=True)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # my apps 
    'accounts',
    'website',
    'shop',
    'cart',
    'order',
    'payment',
    'dashboard',


]
SITE_ID = 1



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_processor',
                'website.context_processors.website_processor',

                
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("PGDB_NAME",default='postgres'),                      
        'USER': config("PGDB_USER",default='postgres'),
        'PASSWORD': config("PGDB_PASSWORD",default='postgres'),
        'HOST': config("PGDB_HOST",default='db'),
        'PORT': config("PGDB_PORT", cast=int,default=5432),
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

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS =  [
    BASE_DIR / 'static'
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = config("EMAIL_HOST",default="smtp4dev")
# EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool ,default=False)
# EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool ,default=False)
# EMAIL_PORT = config("EMAIL_PORT", cast=int,default=25)
# EMAIL_HOST_USER = config("EMAIL_HOST_USER",default="")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD",default="")


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SHOW_DEBUGGER_TOOLBAR = config("SHOW_DEBUGGER_TOOLBAR", cast=bool, default=True)
if SHOW_DEBUGGER_TOOLBAR:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
    
AUTH_USER_MODEL = 'accounts.CustomeUser'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL= '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# password reset link timeout
# PASSWORD_RESET_TIMEOUT = 172800 

MERCHANT_ID = config("MERCHANT_ID",default="4ced0a1e-4ad8-4309-9668-3ea3ae8e8810")
SANDBOX_MODE = config("SANDBOX_MODE", cast=bool, default=True)