import imp
from django.urls import URLPattern, path
from . import views
from django.conf import settings

URLPatterns = [
    path('/', views.home, name='home')
]