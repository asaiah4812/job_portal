from django.contrib import admin
from job.models import Job, JobExp, JobRes

# Register your models here.

admin.site.register([Job, JobRes, JobRes])
