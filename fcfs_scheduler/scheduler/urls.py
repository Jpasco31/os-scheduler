# scheduler/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fcfs_index, name='fcfs_index'),  # Root path now points to `fcfs_index`
    # Keep other URLs if needed, e.g., for SJF or other views
]
