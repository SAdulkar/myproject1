from django.contrib import admin
from django.urls import path,include
from hr import views

urlpatterns = [
    path('login/',views.login,name='login'),
   
]