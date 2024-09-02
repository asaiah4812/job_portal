from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('create-company/', views.create_company, name='create-company'),
    path('update-company/', views.update_company, name='update-company'),
    path('<str:pk>/', views.company, name='company'),
]
