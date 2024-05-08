from django.db import models


from Admin.models import tbl_place,tbl_batch,tbl_subject
# from Teacher.models import *
# from Student.models import *

# Create your models here.
class tbl_section (models.Model):
    section_name=models.CharField(max_length=20)
    section_mark=models.IntegerField()
    section_qstn=models.IntegerField(null=True)

class tbl_student(models.Model):
    student_name=models.CharField(max_length=50)
    student_contact=models.CharField(max_length=15)
    student_email=models.EmailField()
    student_address=models.TextField()
    student_photo=models.FileField(upload_to='StudentDocs/')
    placeid=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
    student_gender=models.CharField(max_length=10)
    batchid=models.ForeignKey(tbl_batch,on_delete=models.CASCADE,null=True)
    student_password=models.CharField(max_length=50,unique=True)
     
class tbl_exam(models.Model):
     exam_date=models.DateField()
     batchid=models.ForeignKey(tbl_batch,on_delete=models.CASCADE, null=True)
     subjectid=models.ForeignKey(tbl_subject,on_delete=models.CASCADE,null=True)
     exam_status=models.IntegerField(default=0)


    

