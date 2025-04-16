import os
import django
from fastapi import FastAPI
from django.core.wsgi import get_wsgi_application
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Mount, Router
from weather_app.main import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

django_app = get_wsgi_application()


application = Router([
    Mount("/weather_app", app=fastapi_app),
    Mount("/", app=WSGIMiddleware(django_app)),
])

