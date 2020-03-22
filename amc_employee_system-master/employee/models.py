from django.db import models


class Employee(models.Model):
	name = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, unique=True)
	address = models.TextField()
	phone = models.IntegerField()

	def __str__(self):
		return self.name