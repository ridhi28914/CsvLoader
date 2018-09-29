from __future__ import unicode_literals

from django.db import models

# Create your models here.
class item(models.Model):
	key=models.CharField(primary_key = True, max_length=1000)
	value=models.IntegerField()
	def __str__(self):
		return self.key
