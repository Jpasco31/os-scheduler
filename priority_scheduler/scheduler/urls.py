# scheduler/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.priority_index, name='priority_index'),
]
