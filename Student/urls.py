from django.urls import path

from Student import  views

app_name='wstudent'

urlpatterns = [
    path('Homepage/', views.Homepage,name="homepage"),
    path('Myprofile/', views.Myprofile,name="myprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),
    path('Viewexam/', views.Viewexam),
    path('Sendcomplaint/', views.Sendcomplaint, name="send_complaint"),
    path('Review/', views.review, name='review'),

    # path('Viewcomplaint/', views.Viewcomplaint),
    path('Answer/<int:qid>/<int:exid>', views.Answer,name="answer"),
    path('ExamReg/<int:id>', views.ExamReg,name="ExamReg"),
    path('Viewquestions/<int:eid>/<int:exid>', views.Viewquestions,name="viewquestions"),
    path('Viewexam/', views.Viewexam,name="viewexam"),
    path('Viewmark/<int:id>', views.Viewmark,name="viewmark"),
    path('AjaxSubject/',views.ajax_subject,name='ajaxsubject'),
    path('', views.Index, name="index"),
    path('Examcompletecheck/<int:exid>', views.Examcompletecheck, name="examcompletecheck"),
    path('timeout/<int:exid>', views.timeout, name="timeout"),

]
