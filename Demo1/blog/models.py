# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)

    class Meta:
        db_table = 'blog'


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
