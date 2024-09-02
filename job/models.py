from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company
import uuid
# Create your models here.

User = get_user_model()

class Job(models.Model):
    PAY_MODE = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )
    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    )
    JOB_LOCATION = (
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Onsite', 'Onsite'),
    )
    JOB_CAT = (
        ('Permanent', 'Permanent'),
        ('Contract', 'Contract'),
    )
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jbs")
    title = models.CharField(max_length=100)
    date_time_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateField(auto_now_add=True)
    pay = models.PositiveIntegerField()
    pay_mode = models.CharField(max_length=30, choices=PAY_MODE)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    job_location = models.CharField(max_length=30, choices=JOB_LOCATION)
    job_cat = models.CharField(max_length=30, choices=JOB_CAT)
    expiry_date = models.DateField(null=True, blank=True)
    hours_per_week = models.PositiveIntegerField()
    job_description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Jobes'


class JobRes(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobExp(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




