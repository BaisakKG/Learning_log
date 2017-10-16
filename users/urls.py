﻿"""Определяем схемы URL для пользовательей"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
            # Страница входа
            url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
            #Страница выхода
            url(r'^logout/$', views.logout_view, name='logout'),
            #Страница регистрации
            url(r'^register/$', views.register,name='register'),
]