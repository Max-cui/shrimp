# -*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    ID = models.CharField(max_length=30,  auto_created=True, unique=True)
    NAME = models.CharField(max_length=30, blank=True)
    PHONE_NUMBER = models.CharField(max_length=30, blank=True)
    EMAIL_ADDRESS = models.CharField(max_length=30, blank=True)