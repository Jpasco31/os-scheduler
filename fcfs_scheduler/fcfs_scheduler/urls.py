# fcfs_scheduler/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduler.urls')),  # Root path points to `scheduler/urls.py`
]
