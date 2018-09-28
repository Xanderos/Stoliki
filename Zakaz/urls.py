from django.contrib import admin
from django.urls import path,include
from Zakaz import views




urlpatterns = [

    path('zak',views.DateView.as_view(),name='home'),
    path('',views.JournalView.as_view(), name='journal'),
    ]
