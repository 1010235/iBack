from .base import *

config_secret_deploy = json.loads(open(SECRET_DEPLOY_JSON_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'


DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']
