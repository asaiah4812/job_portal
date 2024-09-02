from django.contrib.auth import get_user_model
from .models import User, Profile, Company
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


User = get_user_model()
class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password1', 'password2']


class UpdateProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'image', 'country', 'phone', 'bio']

