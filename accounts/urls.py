from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register-recruiter/', views.create_recruiter, name='signup_recruiter'),
    path('register-candidate/', views.create_candidate, name='signup_candidate'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
