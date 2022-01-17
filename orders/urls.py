from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('create', views.order_create, name='order_create'),
]