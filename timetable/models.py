# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Slot(models.Model):
		
		day = models.CharField(max_length=50)
		time = models.BigIntegerField	()
		is_free = models.BooleanField(default=True)	

		def __str__(self):
			return self.day	+ '-' + str(self.time)	


class Event(models.Model):
		slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)
		ename = models.CharField(max_length=250)
		venue = models.CharField(max_length=500)
		code = models.BigIntegerField()

		def __str__(self):
			return self.ename






			