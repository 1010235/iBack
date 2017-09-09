from .base import *

config_secret_deploy = json.loads(open(SECRET_DEPLOY_JSON_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']
S3_USER_SIGV4 = True

# Storage settings
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']
