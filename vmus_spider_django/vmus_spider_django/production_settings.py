# import all default settings
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration
STATIC_ROOT = 'staticfiles'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# STATIC_URL = '/static/'
#
# STATIC_ROOT = join(BASE_DIR, 'assets')
#
# STATICFILES_DIRS = [join(BASE_DIR, 'static')]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (('Alec Hsu', 'hsu022210@gmail.com'),)