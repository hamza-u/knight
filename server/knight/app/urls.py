from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='login'),
    url(r'^login_next/$', views.index, name='login_next'),
    url(r'^$', views.index, name=''),
    url(r'^secure/$', views.secure_page, name='secure'),
	url(r'^client/add/$', views.add_client, name='add_client'),
	url(r'^client/add/next$', views.add_client, name='add_client_next'),

    url(r'^logout/', 'django.contrib.auth.views.logout',{'next_page': '/login'}),
]
