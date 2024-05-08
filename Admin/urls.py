from django.urls import path

from Admin import  views

app_name='wadmin'

urlpatterns = [
    path('Batch/', views.Batch,name="batch"),
    path('delete_batch/<int:id>',views.delete_batch,name="delete_batch"),
    path('edit_batch/<int:eid>',views.edit_batch,name="edit_batch"),


    path('District/', views.District ,name="district"),
    path('EditDistrict/<int:eid>',views.edit_district, name='edit_district'),
    path('delete_district/<int:id>',views.delete_district,name="delete_district"),


    path('Subject/', views.Subject,name="subject"),
    path('delete_subject/<int:id>',views.delete_subject,name="delete_subject"), 
    path('edit_subject/<int:eid>',views.edit_subject,name="edit_subject"),

    path('Exam/', views.Exam,name="exam"),
    path('StartExam/<int:stid>', views.start_exam,name="startexam"),
    path('EndExam/<int:endid>', views.end_exam,name="endexam"),

    path('delete_exam/<int:id>',views.delete_exam,name="delete_exam"),

    path('Place/', views.Place,name="place"),
    path('delete_place/<int:id>',views.delete_place,name="delete_place"),
    path('EditPlace/<int:eid>',views.edit_place, name='edit_place'),

    
    path('AjaxSubject/',views.ajax_subject,name='ajaxsubject'),


    path('Questions/<int:id>', views.Questions,name="questions"),
    path('delete_questions/<int:id>',views.delete_questions,name="delete_questions"),

    path('Homepage/', views.Homepage,name="homepage"),
    
    path('Viewcomplaint/', views.Viewcomplaint,name="Viewcomplaint"),
    path('Reply/<int:cid>', views.ReplyInsert,name="reply"),
 
    path('Teacherverification/', views.Teacherverification,name="teacherverification"),
     path('teacher_accept/<int:aid>',views.teacher_accept,name="teacher_accept"),
    path('teacher_reject/<int:rid>',views.teacher_reject,name="teacher_reject"),

    path('Logout/',views.logout, name="logout"),
    path('Viewreview/', views.Viewreview,name="viewreview"),
]
