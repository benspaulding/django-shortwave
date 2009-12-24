# Django settings for shortwave tests.

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', }}

ROOT_URLCONF = 'shortwave.tests.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'shortwave',
)
