import ptvsd
from .base import *


DEBUG = True

# Hosts
ALLOWED_HOSTS = ['*']
BASE_URL = 'http://127.0.0.1:8000'


# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# run "python -m smtpd -n -c DebuggingServer localhost:1025"
EMAIL_HOST = 'localhost'

# 5678 is the default attach port in the VS Code debug configurations
if False:
    print("Waiting for debugger attach")
    ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.wait_for_attach()
