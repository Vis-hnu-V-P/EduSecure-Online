from django.contrib import admin
from django.urls import path,include

from Teacher import views

app_name='wteacher'


urlpatterns = [
  
    path('Section/', views.Section,name="section"),
    path('delete_section/<int:id>',views.delete_section,name="delete_section"),
     path('edit_section/<int:eid>',views.edit_section, name='edit_section'),
   
    path('Studentregisteration/', views.Studentregisteration,name="studentregistration"),
    path('AjaxPlace', views.ajax_place, name="ajax_place"),
    path('AjaxSubject', views.ajax_subject, name="ajax_subject"),
    path('Myprofile/', views.Myprofile),
    path('Editprofile/', views.Editprofile),
    path('Changepassword/', views.Changepassword,name="Changepassword"),
    path('Viewstudents/<int:eid>/<int:bid>', views.Viewstudent,name="viewstudent"),
   path('Viewanswers/<int:exid>', views.Viewanswers, name="viewanswers"),


    path('Homepage/', views.Homepage,name="homepage"),
    path('Myprofile/', views.Myprofile,name="myprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),

     path('Index', views.Index, name="index"),
     path('Listexam', views.Listview, name="listexam"),
     path('Exammark', views.Exammark, name="exammark"),
     path('Evaluate', views.Evaluate, name="evaluate"),
]