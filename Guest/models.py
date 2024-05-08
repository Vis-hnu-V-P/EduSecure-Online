from django.db import models
from Admin.models import *
from Admin.models import tbl_place
# Create your models here.

class tbl_teacher(models.Model):
    teacher_name=models.CharField(max_length=50)
    teacher_contact=models.CharField(max_length=15)
    teacher_email=models.EmailField()
    teacher_password=models.CharField(max_length=50,unique=True)
    teacher_address=models.TextField()
    teacher_photo=models.FileField(upload_to='TeacherDocs/')
    teacher_proof=models.FileField(upload_to='TeacherDocs/')
    teacher_status=models.IntegerField(default=0)
    teacher_gender=models.CharField(max_length=10)
    place_id=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)