from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from django.urls import reverse
from company.forms import AddCompany, UpdateCompany
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def create_company(request):
    if request.method == 'POST':
        form = AddCompany(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Company.objects.filter(name=name).exists():
                messages.warning(request, 'Company already exists')
            else:
                var = form.save(commit=False)
                var.user = request.user
                user = User.objects.get(pk=request.user.pk)
                var.has_company = True
                var.save()
                user.save()
                messages.success(request, 'Company created successfully')
                return redirect('core:home')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = AddCompany()
    context = {}
    return render(request, 'company/create-company.html', context)

def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompany(request.POST, instance=company)
        if form.is_valid():
            name = request.POST['name']
            if Company.objects.filter(name=name).exists():
                messages.warning(request, 'Company already exists')
            else:
                var = form.save()
                var.user = request.user
                var.save()
                messages.success(request, 'Company information Updated successfully')
                return redirect(reverse('company', args=[company.pk]))
        else:
            messages.error(request, 'Something went wrong')
            return redirect(reverse('company', args=[company.pk]))
    else:
        form = AddCompany(instance=company)
        context = {
            'form':form,
        }
    return render(request, 'company/update-company.html', context)

def company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    context = {'company':company}
    return render(request, 'company/company.html', context)


