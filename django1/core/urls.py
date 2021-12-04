from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato)
]