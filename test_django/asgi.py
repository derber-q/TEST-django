"""ASGI config for test_django project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_django.settings")

application = get_asgi_application()
