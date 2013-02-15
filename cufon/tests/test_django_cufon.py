import os
from tempfile import gettempdir

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'cufon',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        }
}

STATIC_ROOT = os.path.join(gettempdir(), 'cufon-test')
STATIC_URL = '/static/'

DEBUG = True
