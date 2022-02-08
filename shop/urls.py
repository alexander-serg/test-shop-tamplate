from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', item_list, name='home'),
    path('action/', action, name='action'),
    path('sale/', sale, name='sale'),
    path('contact/', contact, name='contact'),
    path('rental/', rental, name='rental'),
    path('category/wedding', wedding_dress, name='wedding'),
    path('category/evening', evening_dress, name='evening'),
    path('category/child', child_dress, name='child'),
    path('post/<slug:post_slug>/', item_detail, name='post'),
]