from django.contrib import admin
from job.models import Job, JobRating, JobReview

admin.site.register(Job)
admin.site.register(JobRating)
admin.site.register(JobReview)