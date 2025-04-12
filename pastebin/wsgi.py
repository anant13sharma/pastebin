"""
WSGI config for pastebin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pastebin.settings')

application = get_wsgi_application()

# Auto-run migrations on Render free tier
if os.environ.get('RENDER'):
    from django.core.management import call_command
    try:
        call_command('migrate')
    except Exception as e:
        print("⚠️ Migration failed:", e)

app = application
