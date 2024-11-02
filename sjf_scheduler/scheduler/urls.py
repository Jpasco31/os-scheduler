# scheduler/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sjf/', views.sjf_index, name='sjf_index'),
]
