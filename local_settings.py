# Local settings for kegbot.
# Edit settings, then copy this file to /etc/kegbot/local_settings.py or
# ~/.kegbot/local_settings.py

# Disable DEBUG mode when serving external traffic.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

### Database configuration
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

### General

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p7jep28p$+7kb8n=qr+1!i80&5d&!2q_lruhs-%rs(urq4)f*j'

### Media and Static Files
import os
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
STATIC_URL = 'http://' + os.environ['AWS_S3_CUSTOM_DOMAIN'] + '/'

### Cache
import urlparse
import json
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
            'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
            'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
        }
    }
}

### Facebook

# Want to use Facebook Connect for registration/login? You will need to set
# these values up to the correct strings.
FACEBOOK_API_KEY = None
FACEBOOK_SECRET_KEY = None

### Twitter

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET_KEY =''

### Foursquare

FOURSQUARE_CLIENT_ID = ''
FOURSQUARE_CLIENT_SECRET = ''
FOURSQUARE_REQUEST_PERMISSIONS = ''

### Untappd

# You'll need an API key from Untappd to enable Untappd features.
UNTAPPD_API_KEY = ''
GMT_OFFSET = '-5'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
