"""
WSGI config for iftar_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.contrib.auth import get_user_model
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iftar_backend.settings')

# This will run ONCE when the app starts
django.setup()

# Create superuser if it doesn't exist
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username='admin',           # Change this
        email='admin@example.com',  # Change this
        password='admin123'         # Change this
    )
    print("✅ Superuser created successfully!")

application = get_wsgi_application()
