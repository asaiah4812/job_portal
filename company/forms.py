from .models import Company
from django.forms import ModelForm

class AddCompany(ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)

class UpdateCompany(ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)
