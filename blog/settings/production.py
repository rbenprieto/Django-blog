from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost:8000', 'localhost','https://djangoblogrubenprieto.herokuapp.com', 'djangoblogrubenprieto.herokuapp.com', 'web-production-72b2.up.railway.app', 'https://web-production-72b2.up.railway.app']

# Database and transactions
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('BLOG_DB_NAME'),
        'USER': os.environ.get('BLOG_DB_USER'),
        'PASSWORD': os.environ.get('BLOG_DB_PASSWORD'),
        'HOST': os.environ.get('BLOG_DB_HOST'),
        'PORT': os.environ.get('BLOG_DB_PORT'),
        'ATOMIC_REQUESTS': True
    }
}
