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

### Timezone and language

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'America/New_York'

### Media and Static Files

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
STATIC_URL = '/static/'

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
