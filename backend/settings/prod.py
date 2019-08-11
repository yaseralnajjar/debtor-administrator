import dj_database_url
from urllib.parse import quote_plus

from .base import *


DEBUG = bool(os.environ.get('DEBUG'))
SECRET_KEY = os.environ.get('SECRET_KEY')

# Hosts
# ALLOWED_HOSTS sample env var: 'www.debtor-admin.com;.debtor-admin.com'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(';')
BASE_URL = os.environ.get('BASE_URL')


# CORS settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = False


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# EMAIL config
"""
Sample env vars:
DEFAULT_FROM_EMAIL = Debtor Administrator <no-reply@debtor-admin.com>
EMAIL_HOST = smtp.mailgun.org
EMAIL_HOST_USER = no-reply@debtor-admin.com
EMAIL_HOST_PASSWORD = MySuperPassword
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True