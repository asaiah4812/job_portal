from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from job.forms import *
from job.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

def create_job(request):
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Job.objects.filter(title=title).exists():
                messages.warning(request, 'Job title already exists')
            else:
                var = form.save(commit=False)
                company = Company.objects.get(pk=request.user.company.pk)
                var.company = company
                var.save()
                messages.success(request, 'New Job created successfully')
                return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = JobCreationForm()
        context = {'form': form}
    return render(request, 'job/create-job.html', context)

def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Job.objects.filter(title=title).exists():
                messages.warning(request, 'Job title already exists')
            else:
                form.save()
                messages.success(request, 'Job Updated successfully')
                return redirect(reverse('job:job', args=[job.pk]))
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
    return render(request, 'job/update-job.html', context)

def delete_job(request, pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    messages.info(request, 'Job deleted successfully')
    return redirect('jobs-per-company')


def job_per_company(request):
    company = Company.objects.get(pk=request.user.company.pk)
    jobs = company.job_set.all()
    context = {'jobs':jobs}
    return render(request, 'job/job_per_company.html', context)

def job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {'job':job}
    return render(request, 'job/job.html', context)

def add_jobres(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobRes(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request, "New Job reponsibility Created")
            return redirect(reverse('job:add-jobres', args=[job.pk]))
        else:
            messages.error(request, "Something went wrong")
            return redirect(reverse('job:add-jobres', args=[job.pk]))
    else:
        form = AddJobRes()
        context = {'form':form}
    return render(request, 'job/add_jobres.html', context)

def add_jobexp(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobExp(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request, "New Job Experience Created")
            return redirect(reverse('job:add-jobexp', args=[job.pk]))
        else:
            messages.error(request, "Something went wrong")
            return redirect(reverse('job:add-jobres', args=[job.pk]))
    else:
        form = AddJobExp()
        context = {'form':form}
    return render(request, 'job/add_jobexp.html', context)



def delete_jobres(request, pk):
    jobres = JobRes.objects.get(pk=pk)
    get_job = jobres.job
    jobres.delete()
    messages.info(request, "Job Responsibility deleted")
    return redirect(reverse('job:job', args=[get_job.pk]))

def delete_jobexp(request, pk):
    jobexp = JobExp.objects.get(pk=pk)
    get_job = jobexp.job
    jobexp.delete()
    messages.info(request, "Job Experience deleted")
    return redirect(reverse('job:job', args=[get_job.pk]))