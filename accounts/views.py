from django.shortcuts import render, redirect
from .models import User, Profile
from django.contrib import messages
from .forms import RegisterUser, UpdateProfile
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

def create_candidate(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            var = form.save()
            var.is_candidate = True
            var.save()
            messages.success(request, 'Candidate Account Created Successfully Login to Continue')
            return redirect('accounts:login')
        else:
            messages.error(request, 'something went wrong')
    else:
        form = RegisterUser()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup_candidate.html', context)


def create_recruiter(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            var = form.save()
            var.is_recruiter = True
            var.save()
            messages.success(request, 'Recruiter Account Created Successfully Login to Continue')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = RegisterUser()
    context = {'form':form}
    return render(request, 'accounts/signup_recruiter.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'User Login Successfully')
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Something went wrong')
    else:
        return render(request, 'accounts/login.html')


def user_profile(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)


def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form':form
        }
    return render(request, 'accounts/update-profile.html', context)
