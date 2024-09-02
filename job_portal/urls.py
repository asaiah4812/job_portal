from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('company/', include('company.urls', namespace='company')),
    path('job/', include('job.urls', namespace='job')),
]
