# Local settings for kegbot.
# Edit settings, then copy this file to /etc/kegbot/local_settings.py or
# ~/.kegbot/local_settings.py
import os

# Disable DEBUG mode when serving external traffic.
DEBUG = False
TEMPLATE_DEBUG = DEBUG

### Database configuration
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

### General

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

### Media and Static Files
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']

KEGBOT_ROOT = ''

# Absolute path to the directory where uploaded media (profile pictures, etc)
# should go.
#MEDIA_ROOT = '/path/to/media/'

# URL of the directory above. The default is '/media/'. Note that the directory
# name given in MEDIA_ROOT does not affect this.
MEDIA_URL = '/media/'

# A directory where non-media static files will be stored. You should create
# this directory, and use 'kegbot collectstatic' to fill it.
STATIC_ROOT = ''

# URL of the directory above. The default is '/static/'. Note that the directory
# name given in STATIC_ROOT does not affect this.
STATIC_URL = '//%s/' % AWS_S3_CUSTOM_DOMAIN

### Cache
from memcacheify import memcacheify
CACHES = memcacheify()

### Celery
BROKER_POOL_LIMIT = 5
BROKER_URL = os.environ['REDISTOGO_URL']
BROKER_TRANSPORT_OPTIONS = {
        'max_connections': 1,
        }
CELERY_RESULT_BACKEND = os.environ['REDISTOGO_URL']
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERY_ALWAYS_EAGER = True

### E-mail
EMAIL_BACKEND = 'sgbackend.SendGridBackend'
EMAIL_FROM_ADDRESS = os.environ['EMAIL_FROM_ADDRESS']
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

from pykeg.settings import LOGGING
LOGGING['handlers']['redis']['url'] = os.environ['REDISTOGO_URL']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
