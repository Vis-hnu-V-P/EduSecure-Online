from django.contrib import admin
from django.urls import path,include

from Guest import views

app_name='wguest'

urlpatterns = [
  
     path('Teacherregisteration/', views.Teacherregisteration,name="teacherregisteration"),
     path('Login/', views.Login,name="login"),
     path('AjaxPlace', views.ajax_place, name="ajax_place"),
     path('AjaxSubject', views.ajax_subject, name="ajax_subject"),
     path('', views.Index, name="index"),

]