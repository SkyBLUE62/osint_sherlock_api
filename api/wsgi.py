"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/var/task/execution')
sys.path.append('/execution')
sys.path.append('/execution/sherlock')
sys.path.append('/execution/sherlock/sherlock_project')
sys.path.append('/var/task/execution')
sys.path.append('/var/task/execution/sherlock/sherlock_project')
sys.path.append('/var/task/execution/sherlock')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()

app = get_wsgi_application()
