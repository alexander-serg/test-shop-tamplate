from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', item_list, name='home'),
    path('about/', about, name='about'),
    path('service', service, name='service'),
    path('contact/', contact, name='contact'),
    path('inst/', inst, name='inst'),
    path('post/<slug:post_slug>/', item_detail, name='post'),
]