from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--=%-7ozj&qzgt7qno&a0qgkj5!a9f33*z(#1ytfgo2!rm)!6j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mahdior.com','www.mahdior.com']

#INSTALLED_APPS = []

SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mahdiorc_miracle',
        'USER': 'mahdiorc_mahdi',
        'PASSWORD': 'mahdikaka1380',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
STATIC_ROOT = '/home/mahdiorc/public_html/static'
MEDIA_ROOT = '/home/mahdiorc/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'