from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=False)
    has_company = models.BooleanField(default=False)
    has_resume = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar/default.jpg')
        return avatar