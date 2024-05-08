from django.db import models

from Admin.models import tbl_questions
from Teacher.models import tbl_exam, tbl_student
from Student.models import *



# Create your models here.

class tbl_review(models.Model):
    review_rating=models.IntegerField()
    review_content=models.CharField(max_length=100)
    review_date=models.DateTimeField()
    student_id = models.ForeignKey(tbl_student,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=50)
    complaint_content = models.CharField(max_length=100)
    complaint_reply = models.CharField(max_length=100)
    status=models.IntegerField(default=0)
    student = models.ForeignKey(tbl_student, on_delete=models.CASCADE)
    # exam_id = models.ForeignKey(tbl_exam, on_delete=models.CASCADE)



class tbl_examstudent(models.Model):
    student_id=models.ForeignKey(tbl_student,on_delete=models.CASCADE, null=True)
    exam_id=models.ForeignKey(tbl_exam,on_delete=models.CASCADE, null=True)
    answer_mark=models.IntegerField(default=0)
    exam_status=models.IntegerField(default=0)

class tbl_answer(models.Model):
    answer_content=models.CharField(max_length=500)
    question_id= models.ForeignKey(tbl_questions,on_delete=models.CASCADE)
    exstudent_id = models.ForeignKey(tbl_examstudent,on_delete=models.CASCADE)
    answer_mark=models.IntegerField(null=True)

