from django.http import JsonResponse
from django.shortcuts import render,redirect
from Student.models import tbl_answer, tbl_examstudent
from Teacher.models import * 
from Admin.models import *
from Guest.models import *
from django.db.models import Sum

# Create your views here.
def Section(request):
      Section = tbl_section.objects.all()
      if request.method=="POST":
           tbl_section.objects.create(section_name=request.POST.get("txt_section"),section_mark=request.POST.get("txt_mark"),section_qstn=request.POST.get("txt_qstn"))
           return redirect("wteacher:section") 
      else:
         return render(request,"Teacher/Section.html",{"section":Section})
def delete_section(request,id):
     tbl_section.objects.get(id=id).delete()
     return redirect("wteacher:section")

def edit_section(request,eid):
     section = tbl_section.objects.all()
     data=tbl_section.objects.get(id=eid)


def Studentregisteration(request):
    batch=tbl_batch.objects.all()
    district=tbl_district.objects.all()
    studentdata = tbl_student.objects.all()
    if request.method=="POST":
          placeid=tbl_place.objects.get(id=request.POST.get("txt_place"))

          tbl_student.objects.create(student_name=request.POST.get("txt_name"),
                                            student_contact=request.POST.get("txt_contact"),
                                            student_email=request.POST.get("txt_email"),
                                            student_address=request.POST.get("txt_address"),
                                            student_photo=request.FILES.get("txt_photo"),
                                            placeid=placeid,
                                            student_gender=request.POST.get("gender"),
                                            # student_batch=request.POST.get("txt_batch"),
                                            student_password=request.POST.get("txt_password")
                                            )
          return redirect('wteacher:studentregistration')
    else:
        return render(request,"Teacher/Studentregisteration.html",{'studentreg':studentdata,'district':district,'batch':batch})
    
def ajax_place(request):
    distid=tbl_district.objects.get(id=request.GET.get("disid"))
    place_data=tbl_place.objects.filter(district_id=distid)
    return render(request,"Guest/AjaxPlace.html",{'Place':place_data})


def ajax_subject(request):
    batch=tbl_batch.objects.get(id=request.GET.get("bsid"))
    subject_data=tbl_subject.objects.filter(batch_id=batch)
    return render(request,"Teacher/AjaxSubject.html",{'subject':subject_data})

def Myprofile(request):
    teacherdata=tbl_teacher.objects.get(id=request.session['tid'])
    return render(request,"Teacher/Myprofile.html",{'teacher':teacherdata})
def Editprofile(request):
            teacherdata=tbl_teacher.objects.get(id=request.session['tid'])
            if request.method=='POST':
                teacherdata.teacher_name=request.POST.get("txt_name")
                teacherdata.teacher_email=request.POST.get("txt_email")
                teacherdata.teacher_contact=request.POST.get("txt_contact")
                teacherdata.teacher_address=request.POST.get("txt_address")
                teacherdata.save()
                return redirect('wteacher:myprofile')
            else:
                return render(request,"Teacher/EditProfile.html",{'teacher':teacherdata})
def Changepassword(request):
     teacherdata=tbl_teacher.objects.get(id=request.session['tid'])
     if request.method=="POST":
          currentpswd=request.POST.get("CurrentPassword")
          print(currentpswd)
          newpswd=request.POST.get("NewPassword")
          confirmpswd=request.POST.get("ConfirmPassword")
          if teacherdata.teacher_password == currentpswd:
               if newpswd == confirmpswd :
                    teacherdata.teacher_password=request.POST.get("NewPassword")
                    teacherdata.save()
                    return render(request,'Teacher/MyProfile.html' , {"msg":"Password Changed Successfully" })
               else:
                    msg="PASSWORD MISMATCH"
                    return render(request,'Teacher/ChangePassword.html',{'msg':msg})
          else:
                msg="INVALID CURRENT PASSWORD"
                return render(request,'Teacher/ChangePassword.html',{'msg':msg})
     else:
             return render(request,"Teacher/ChangePassword.html")     
        
def Viewstudent(request,eid,bid): 
    print('Exam:',eid)
    print('Batch:',bid)
    exstudent = tbl_examstudent.objects.all() 
    if request.method=="POST":
          return redirect('wteacher:viewstudent')
    else:
        return render(request, "Teacher/Viewstudent.html", {'exstudents': exstudent})
    

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

def Evaluate(request):
    try:
        answer = tbl_answer.objects.get(id=request.POST.get("aid"))
        answer.answer_mark = request.POST.get("mark")
        answer.save()
        return JsonResponse({'message': 'Mark updated successfully'})
    except tbl_answer.DoesNotExist:
        return JsonResponse({'message': 'Answer not found'}, status=404)

def Homepage(request):
    teacher = tbl_teacher.objects.get(id=request.session["tid"])
    return render(request,"Teacher/Homepage.html",{
        'teacher':teacher
    })
    
def Index(request):
    if request.method=="POST":
         return render(request,"Teacher/index.html")
    else:
         return render(request,"Teacher/index.html")

def Listview(request):
    batch = tbl_batch.objects.all()
    if request.method == "POST":
        print('Hi')
        batch_id=tbl_batch.objects.get(id=request.POST.get("ddl_batch"))
        teacher=tbl_teacher.objects.get(id=request.session["tid"])
        sub_id=teacher.subject_id.id
        print(sub_id)
        subject=tbl_subject.objects.get(id=sub_id)
        exam=tbl_exam.objects.filter(batchid_id=batch_id,subjectid_id=subject)
        return render(request, "Teacher/Listexam.html", {'exam': exam,'batch':batch,'bid':request.POST.get("ddl_batch")})
    else:
        return render(request, "Teacher/Listexam.html", {'batch':batch})

def Exammark(request):
     if request.method == "POST":
          return render(request,"Teacher/Exammark.html")
     else:
          return render(request,"Teacher/Exammark.html")
          
