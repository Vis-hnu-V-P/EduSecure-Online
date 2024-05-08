from django.db import models

# from Teacher.models import tbl_section 


# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_batch(models.Model):
    batch_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district_id=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)

class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=50)
    batch_id=models.ForeignKey(tbl_batch,on_delete=models.CASCADE,null=True)


class tbl_reply(models.Model):
    reply=models.CharField(max_length=100)
   
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True)
    admin_password=models.CharField(max_length=50)


from Teacher.models import tbl_exam,tbl_section
from Guest.models import *

class tbl_questions(models.Model):
    question=models.CharField(max_length=50)
    sectiondata=models.ForeignKey(tbl_section, on_delete=models.CASCADE)
    batchdata=models.ForeignKey(tbl_batch, on_delete=models.CASCADE)
    subjectdata=models.ForeignKey(tbl_subject, on_delete=models.CASCADE)
    exam_id=models.ForeignKey(tbl_exam, on_delete=models.CASCADE, null=True)



class tbl_examanswer(models.Model):
    examanswer_content=models.CharField(max_length=2048)
    examanswer_mark=models.IntegerField
    teacher_id=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)
