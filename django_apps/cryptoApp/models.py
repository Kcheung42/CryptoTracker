# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Crypto(models.Model):
	name = models.CharField(max_length=500)
	symbol = models.CharField(max_length=500)
	image = models.ImageField(null=True, blank=True)
	tool = models.CharField(max_length=500)
	price = models.FloatField(default=0)

	def __str__(self):
		return self.name
