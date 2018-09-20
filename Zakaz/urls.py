from django.contrib import admin
from django.urls import path,include
from Zakaz import views




urlpatterns = [

    path('',views.zakaz,name='home'),

    ]
