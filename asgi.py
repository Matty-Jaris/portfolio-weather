import os
import django
from fastapi import FastAPI
from weather_app.main import app as fastapi_app
from django.core.asgi import get_asgi_application
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Mount, Router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

# Kombinace Django + FastAPI
django_app = get_asgi_application()

application = Router([
    Mount("/", app=WSGIMiddleware(django_app)),
    Mount("/weather_app", app=fastapi_app),
])
