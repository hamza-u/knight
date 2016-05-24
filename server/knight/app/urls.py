from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='login'),
    url(r'^accounts/login$', views.index, name='welcome'),
    url(r'^login_next/$', views.index, name='login_next'),
    url(r'^$', views.index, name=''),
    url(r'^secure/$', views.secure_page, name='secure'),
    url(r'^logout/', 'django.contrib.auth.views.logout',{'next_page': '/login'}),
]
