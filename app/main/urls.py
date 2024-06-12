from os import name
from django.urls import path

from main.views import index, catalog, cart

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('cart/', cart, name='cart')
]
