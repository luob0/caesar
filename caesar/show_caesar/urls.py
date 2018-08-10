# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


app_name = 'show_caesar'
urlpatterns = [
    url(r'^$', views.showcaesar, name='caesar'),
    #url(r'^caesar$', views.showcaesar, name='caesar'),
]
