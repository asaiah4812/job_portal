from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
import uuid

User = get_user_model()
# Create your models here.

class Company(models.Model):
    STATE = (
        ('abuja', 'Abuja'),
        ('adamawa', 'Adamawa'),
        ('taraba', 'Taraba'),
        ('kaduna', 'Kaduna'),
        ('lagos', 'Lagos'),
        ('jos', 'Jos'),
    )
    INDUSTRY = (
        ('Software', 'Software'),
        ('Finance', 'Finance'),
        ('Education', 'Education'),
    )
    SIZE=(
        ('1 - 15', '1 - 15'),
        ('15 - 40', '15 - 40'),
        ('40 - 70', '40 - 70'),
        ('70 - 200', '70 - 200'),
    )
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=100)
    country = CountryField()
    state = models.CharField(max_length=100, choices=STATE)
    primary_industry = models.CharField(max_length=100, choices=INDUSTRY)
    phone_number = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    company_size = models.CharField(max_length=100, choices=SIZE)
    founded_in = models.PositiveIntegerField()
    linkedin = models.UUIDField()
    twitter = models.UUIDField()
    website = models.UUIDField()

    def __str__(self):
        return self.name