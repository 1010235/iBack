from .base import *

config_secret_debug = json.loads(open(SECRET_DEPLOY_JSON_FILE).read())

WSGI_APPLICATION = 'config.wsgi.debug.application'

INSTALLED_APPS.append('django_extensions')


DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']


