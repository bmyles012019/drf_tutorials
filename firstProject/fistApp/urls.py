

from django.urls import path, include
from fistApp import views

urlpatterns = [
    path('emps/', views.employeeView ),
]