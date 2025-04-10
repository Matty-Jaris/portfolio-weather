import os
import django
from fastapi import FastAPI
from weather_app.main import app as fastapi_app
from django.core.wsgi import get_wsgi_application
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Mount, Router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

# Django jako WSGI aplikace
django_app = get_wsgi_application()

# Kombinace Django + FastAPI
application = Router([
    Mount("/", app=WSGIMiddleware(django_app)),
    Mount("/weather_app", app=fastapi_app),
])
