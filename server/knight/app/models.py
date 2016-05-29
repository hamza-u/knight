from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
	
class Client(models.Model):
    client_id = models.IntegerField()
    client = models.CharField(max_length=64)
    partner = models.CharField(max_length=20)
    handler = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
