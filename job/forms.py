from django.forms import ModelForm
from job.models import Job, JobExp, JobRes

class JobCreationForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_time_posted', 'date_posted', 'is_published')

class UpdateJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_time_posted', 'date_posted', 'is_published')


class AddJobRes(ModelForm):
    class Meta:
        model = JobRes
        fields = ['name']

class AddJobExp(ModelForm):
    class Meta:
        model = JobExp
        fields = ['name']