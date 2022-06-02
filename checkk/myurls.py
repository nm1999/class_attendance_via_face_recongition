from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.login, name="login"),
   path('dashboard/',views.home, name='home'),
   path('new/',views.newstd,name='newstd'),
   path('print/',views.printout, name="print"),
]