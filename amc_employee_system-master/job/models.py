from django.db import models
from users.models import User

"""

title: python developer
description : a very experienced python dev.
category : IT
location : ghorahi
qualification : Bacholer
experience_year : 5
salary : 50000
job_type : full_time


"""

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	category = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	qualification = models.CharField(max_length=255)
	experience_year = models.IntegerField()
	salary = models.IntegerField()
	job_type = models.CharField(max_length=255)
	deadline = models.DateField()
	skills = models.TextField()

	class Meta:
		db_table = "job_job"

	def __str__(self):
		return self.title

class JobRating(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	rating = models.IntegerField()

	def __str__(self):
		return self.user.username + str(self.rating)

class JobReview(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	review = models.TextField()

	def __str__(self):
		return self.user.username + self.review

