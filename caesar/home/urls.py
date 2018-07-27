# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
]
