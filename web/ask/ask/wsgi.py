"""
WSGI config for ask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
#sys.path.append('home/box/web/ask/ask/settings.py')
#sys.path.append('home/box/web/ask/ask')
#sys.path.append('home/box/web/ask')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
