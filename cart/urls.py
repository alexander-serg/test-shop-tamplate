from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:post_id>', views.cart_add, name='cart_add'),
    path('remove/<int:post_id>', views.cart_remove, name='cart_remove'),
    ]