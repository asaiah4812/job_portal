from django.urls import path
from . import views

app_name='job'

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),

]
