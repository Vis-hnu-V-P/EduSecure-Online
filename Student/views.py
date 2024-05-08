from datetime import date
from django.shortcuts import render,redirect
from Admin.models import tbl_batch, tbl_questions, tbl_subject
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from Student.models import *
from Student.models import tbl_answer
from Teacher.models import tbl_exam, tbl_section, tbl_student

# Create your views here.
def Homepage(request):
    student = tbl_student.objects.get(id=request.session["sid"])
    return render(request,"Student/Homepage.html",{
        'student':student
    })


def Myprofile(request):
    studentdata=tbl_student.objects.get(id=request.session['sid'])
    return render(request,"Student/Myprofile.html",{'student':studentdata})
def Editprofile(request):
            studentdata=tbl_student.objects.get(id=request.session['sid'])
            if request.method=='POST':
                studentdata.student_name=request.POST.get("txt_name")
                studentdata.student_email=request.POST.get("txt_email")
                studentdata.student_contact=request.POST.get("txt_contact")
                studentdata.student_address=request.POST.get("txt_address")
                studentdata.save()
                return redirect('wstudent:myprofile')
            else:
                return render(request,"Student/EditProfile.html",{'student':studentdata})
def Changepassword(request):
     studentdata=tbl_student.objects.get(id=request.session['sid'])
     if request.method=="POST":
          currentpswd=request.POST.get("CurrentPassword")
          print(currentpswd)
          newpswd=request.POST.get("NewPassword")
          confirmpswd=request.POST.get("ConfirmPassword")
          if studentdata.student_password == currentpswd:
               if newpswd == confirmpswd :
                    studentdata.student_password=request.POST.get("NewPassword")
                    studentdata.save()
                    return render(request,'Student/MyProfile.html' , {"msg":"Password Changed Successfully" })
               else:
                    msg="PASSWORD MISMATCH"
                    return render(request,'Student/ChangePassword.html',{'msg':msg})
          else:
                msg="INVALID CURRENT PASSWORD"
                return render(request,'Student/ChangePassword.html',{'msg':msg})
     else:
             return render(request,"Student/ChangePassword.html")



def Sendcomplaint(request):
     if request.method == "POST":
          title = request.POST.get("txt_title")
          description = request.POST.get("txt_description")
            
          # Get student ID from session
          student = tbl_student.objects.get(id=request.session['sid'])
          
          tbl_complaint.objects.create(
               complaint_title=title,
               complaint_content=description,
               student=student,
               status=0
          )
          return redirect('wstudent:homepage')
     else:
          return render(request, 'Student/Sendcomplaint.html')

# def Sendcomplaint(request):
#     try:
#         if request.method == "POST":
            # Retrieve data from the form
          #   title = request.POST.get("txt_title")
          #   description = request.POST.get("txt_description")
            
            # Get student ID from session
          #   student_id = request.session.get('sid')
            
            # Check if student ID is present in session
          #   if student_id:
                # Get student object
               #  student = tbl_student.objects.get(id=student_id)
                
                # Create the complaint without associating it with any exam
               #  tbl_complaint.objects.create(
               #      complaint_title=title,
               #      complaint_content=description,
               #      student=student,
               #      complaint_status=0
               #  )
                
                # Redirect after successful form submission to avoid form resubmission on page refresh
          #       return redirect('wstudent:homepage')
          #   else:
                # Handle the case when student ID is not found in session
                # Redirect the user to the login page or display an error message
     #            return redirect('login_url')
     #    else:
            # Render the complaint submission form
          #   return render(request, 'Student/Sendcomplaint.html')
#     except tbl_student.DoesNotExist:
#         # Handle the case when no student is found with the provided student ID
#         # Redirect the user to the login page or display an error message
#         return redirect('login_url')
#     except Exception as e:
#         # Handle other exceptions if necessary
#         return HttpResponse("An error occurred: {}".format(str(e)))

# def review(request):
#     us=tbl_student.objects.get(id=request.session["uid"])
#     userdata=tbl_review.objects.filter(user=us)
#     if request.method=="POST":
#         review.objects.create(review_content=request.POST.get('ufdbk'),user=us)
#         return redirect("wstudent:homepage")
#     else:
#         return render(request,"Student/Review.html",{'userfeed':userdata})
    
def review(request):
     if request.method == "POST":
          description = request.POST.get("txt_reviewdescription")
          rating = request.POST.get("rating")
          # reviewdate = request.POST.get("txt_reviewdate")

            
          # Get student ID from session
          student =tbl_student.objects.get(id=request.session['sid'])
          
          tbl_review.objects.create(
               review_content=description,
               review_rating=rating,
               review_date=date.today(),
               student_id=student
          )
          return redirect('wstudent:homepage')
     else:
          return render(request, 'Student/Review.html')

def Answer(request,qid,exid):
     question=tbl_questions.objects.get(id=qid)
     student=tbl_student.objects.get(id=request.session['sid'])
     exstudent=tbl_examstudent.objects.get(id=exid)
     answercount=tbl_answer.objects.filter(question_id=question,exstudent_id=exstudent).count()
     if answercount>0:
          answer=tbl_answer.objects.get(question_id=question,exstudent_id=exstudent)
          return render(request,"Student/Answer.html/",{'question':question,'answer':answer})
     else:     
          if request.method=="POST":
               tbl_answer.objects.create(answer_content=request.POST.get("txt_answer"),question_id=question,exstudent_id=exstudent,)
               return redirect("wstudent:answer", qid,exid)
          else:
               return render(request,"Student/Answer.html/",{'question':question,'student':student,})
def Viewmark(request):
    if request.method=="POST":
         return render(request,"Student/Viewmark.html/")
    else:
         return render(request,"Student/Viewmark.html/")
    
def ExamReg(request,id):
     exam=tbl_exam.objects.get(id=id)
     student=tbl_student.objects.get(id=request.session['sid'])
     data=tbl_examstudent.objects.create(student_id=student,exam_id=exam)
     exid=data.id
     return redirect("wstudent:viewquestions",id,exid )

    
def Viewquestions(request,eid,exid):
     exam=tbl_exam.objects.get(id=eid)
     section = tbl_section.objects.all()
     subid=exam.subjectid.id
     subject = tbl_subject.objects.get(id=subid)
     eQstn=[]
     for i in section:
          questions = tbl_questions.objects.filter(sectiondata=i,
                                                   subjectdata=subject
                                                   )
          # question_ids = []
          qdata=[]
          for q in questions:
               
               qdata.append(q)
          eQstn.append({'section':i.section_name, 'examqst':qdata})
     return render(request,"Student/Viewquestions.html",{'exam':eQstn,'exid':exid})

def timeout(request, exid):
    student = get_object_or_404(tbl_examstudent, id=exid)
    student.exam_status = 1
    student.save()
    return redirect('wstudent:homepage')

def Examcompletecheck(request,exid):
     student = tbl_examstudent.objects.get(id=exid)
     answer = tbl_answer.objects.filter(exstudent_id=student).count()
     exam_id = student.exam_id_id 
     if answer < 18:
        messages.success(request, 'Exam not Completed Please Complete it.')
        return redirect('wstudent:viewquestions',exam_id,exid)
     else:
          examdata=tbl_examstudent.objects.get(id=exid)
          examdata.exam_status=2
          examdata.save()
          messages.success(request, 'Exam Finished GoodLuck.')
          return redirect('wstudent:homepage')   
          
def Viewmark(request,id):
         answer = tbl_answer.objects.filter(exstudent_id__student_id=request.session["sid"],exstudent_id__exam_id=id)
         total_marks = tbl_answer.objects.filter(exstudent_id__student_id=request.session["sid"],exstudent_id__exam_id=id).aggregate(total_marks=Sum('answer_mark'))['total_marks']  
         return render(request,"Student/Viewmarks.html",{"answers": answer , "total_answers": total_marks})

def Viewanswers(request, exid):
    answers = tbl_answer.objects.filter(exstudent_id=exid)
    total_marks = tbl_answer.objects.filter(exstudent_id=exid).aggregate(total_marks=Sum('answer_mark'))['total_marks']
    print(total_marks)
    if request.method=="POST":
         status=tbl_examstudent.objects.get(id=exid)
         status.exam_status=2
         status.answer_mark=total_marks
         print(type(total_marks))
         status.save()
         return render(request,"Teacher/Homepage.html")  
    return render(request, "Teacher/Viewanswers.html", {"exid": exid, "answers": answers ,  "total_answers": total_marks})
    
def Viewexam(request):
    user = tbl_student.objects.get(id=request.session['sid'])
    batch = tbl_batch.objects.all()
    subject = tbl_subject.objects.all()
    exam = tbl_exam.objects.all()
    if request.method=="POST":
        sub_id = tbl_subject.objects.get(id=request.POST.get("ddl_subject"))
        exam=tbl_exam.objects.filter(subjectid_id=sub_id)
        
        exam_sel = request.POST.get("ddl_subject")

        try:
            mark = tbl_examstudent.objects.get(student_id=user, exam_status=2, exam_id=exam_sel)
            # Query executed successfully, process the result here
        except tbl_examstudent.DoesNotExist:
            # Query returned no results, handle the case here
            mark = None  # or any other default value you want to assign

        return render(request,"Student/Viewexam.html",{'exam':exam, 'batch':batch, 'subject':subject , 'mark':mark})
    else:
        return render(request,"Student/Viewexam.html",{'batch':batch, 'subject':subject }) 
    

def ajax_subject(request):
    bthid=tbl_batch.objects.get(id=request.GET.get("bthid"))
    subject_data=tbl_subject.objects.filter(batch_id=bthid)
    return render(request,"Student/AjaxSubject.html",{'Subject':subject_data})

def Index(request):
    if request.method=="POST":
         return render(request,"Student/index.html")
    else:
         return render(request,"Student/index.html")
    

    
