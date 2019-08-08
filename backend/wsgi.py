import os

from django.core.wsgi import get_wsgi_application

# This will set production as default, but we must still set it with an
# ENV on heroku to ensure that the migrate command runs agains the correct DB
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
