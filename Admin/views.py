from django.shortcuts import render,redirect
from django.contrib import messages
from Admin.models import *
from Student.models import tbl_complaint, tbl_review
from Teacher.models import *
from Guest.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def Batch(request):
    batch = tbl_batch.objects.all()
    if request.method=="POST":
         tbl_batch.objects.create(batch_name=request.POST.get("txt_batch"))
         return redirect("wadmin:batch")
    else:
         return render(request,"Admin/Batch.html/",{"batch":batch})

def delete_batch(request,id):
     tbl_batch.objects.get(id=id).delete()
     return redirect("wadmin:batch")

def edit_batch(request,eid):
     batch = tbl_batch.objects.all()
     data=tbl_batch.objects.get(id=eid)
     
     if request.method == 'POST':
          print(data.batch_name)
          data.batch_name=request.POST.get("txt_batch")
          data.save()
          return  redirect('wadmin:batch')
     else:
          return render(request,'Admin/Batch.html',{
               "Edit":data,
               "batch":batch
          })
def District(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
         tbl_district.objects.create(district_name=request.POST.get("txt_district"))
         return redirect("wadmin:district")
    else:
          return render(request,"Admin/District.html",{"district":district})
def delete_district(request,id):
     tbl_district.objects.get(id=id).delete()
     return redirect("wadmin:district")

def edit_district(request,eid):
     district = tbl_district.objects.all()
     data=tbl_district.objects.get(id=eid)
     
     if request.method == 'POST':
          print(data.district_name)
          data.district_name=request.POST.get("txt_district")
          data.save()
          return  redirect('wadmin:district')
     else:
          return render(request,'Admin/District.html',{
               "Edit":data,
               "district":district
          })

def Subject(request):
    subject = tbl_subject.objects.all()
    batch = tbl_batch.objects.all()
    if request.method=="POST":
          bth_id = tbl_batch.objects.get(id=request.POST.get("ddl_batch"))
          tbl_subject.objects.create(subject_name=request.POST.get("txt_subject") , batch_id = bth_id)
          return redirect("wadmin:subject")
    else:
         return render(request,"Admin/Subject.html/",{"subject":subject,"batch":batch})
    
def delete_subject(request,id):
     tbl_subject.objects.get(id=id).delete()
     return redirect("wadmin:subject")

def edit_subject(request,eid):
     batch = tbl_batch.objects.all()
     subject = tbl_subject.objects.all()
     data=tbl_subject.objects.get(id=eid)
     
     if request.method == 'POST':
          print(data.subject_name)
          bth_id = tbl_batch.objects.get(id=request.POST.get("ddl_batch"))
          data.subject_name=request.POST.get("txt_subject")
          data.batch_id=bth_id
          data.save()
          return  redirect('wadmin:subject')
     else:
          return render(request,'Admin/Subject.html',{
               "Edit":data,
               "subject":subject,"batch":batch
          })
def ajax_subject(request):
    batch=tbl_batch.objects.get(id=request.GET.get("bsid"))
    subject_data=tbl_subject.objects.filter(batch_id=batch)
    return render(request,"Admin/AjaxSubject.html",{'subject':subject_data})

def Place(request):
     District=tbl_district.objects.all()
     place = tbl_place.objects.all()
     if request.method=="POST":
         dis_id = tbl_district.objects.get(id=request.POST.get("ddl_district"))
         tbl_place.objects.create(place_name=request.POST.get("txt_place"),district_id = dis_id)
         return redirect("wadmin:place")
     else:
         return render(request,"Admin/Place.html/",{"place":place,"district":District})
     
def delete_place(request,id):
     tbl_place.objects.get(id=id).delete()
     return redirect("wadmin:place")

def edit_place(request,eid):
     District=tbl_district.objects.all()
     place = tbl_place.objects.all()
     data=tbl_place.objects.get(id=eid)
     
     if request.method == 'POST':
          print(data.place_name)
          dis_id = tbl_district.objects.get(id=request.POST.get("ddl_district"))
          data.place_name=request.POST.get("txt_place")
          data.district_id=dis_id
          data.save()
          return  redirect('wadmin:place')
     else:
          return render(request,'Admin/Place.html',{
               "Edit":data,
               "place":place,
               "district":District
          })

def Questions(request,id):
    section = tbl_section.objects.all()
    batch = tbl_batch.objects.all()
    subject = tbl_subject.objects.all()
    question = tbl_questions.objects.all()

    if request.method == "POST":
        sec_id = tbl_section.objects.get(id=request.POST.get("ddl_section"))
        bth_id = tbl_batch.objects.get(id=request.POST.get("ddl_batch"))
        sub_id = tbl_subject.objects.get(id=request.POST.get("ddl_subject"))
        exam_id = tbl_exam.objects.get(id=id)
        qstcount=tbl_questions.objects.filter(exam_id=exam_id,sectiondata=sec_id).count()
        print(qstcount)
        print('section')
        print(sec_id.section_qstn)
        if(qstcount<sec_id.section_qstn):
          tbl_questions.objects.create(question=request.POST.get("txt_question"), sectiondata=sec_id, batchdata=bth_id, subjectdata=sub_id,exam_id=exam_id )
          messages.success(request, 'Question inserted successfully!')
          return redirect("wadmin:questions", id)
        else:
          messages.success(request, 'Question Count Exceeded')
          return redirect("wadmin:questions", id)
    else:
         return render(request, "Admin/Questions.html", {
              "question": question,
              "section": section,
              "batch": batch,
              "subject": subject
         })
    
def delete_questions(request,id):
     question=tbl_questions.objects.get(id=id)
     nid=question.exam_id.id
     question.delete()
     return redirect("wadmin:questions",nid)
    
def Homepage(request):
    admin = tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/Homepage.html",{
        'admin':admin
    })

def Viewcomplaint(request):
    complaints = tbl_complaint.objects.all()
    if request.method=="POST":
         return render(request,"Admin/Viewcomplaint.html/",{'Complaint':complaints})
    else:
         return render(request,"Admin/ViewComplaint.html/",{'Complaint':complaints})
    
    
def ReplyInsert(request,cid):
    comp=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        comp.complaint_reply=request.POST.get('comprply')
        comp.status=1
        comp.save()
        return redirect("wadmin:Viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")

    
def Teacherverification(request):
    teacherdata=tbl_teacher.objects.filter(teacher_status=0)
    accepted=tbl_teacher.objects.filter(teacher_status=1)
    rejected=tbl_teacher.objects.filter(teacher_status=2)
    return render(request,'Admin/Teacherverification.html',{
        'teachers':teacherdata,
        'teacher_accept':accepted,
        'teacher_reject':rejected,

    })

def teacher_accept(request,aid):
    teacherdata=tbl_teacher.objects.get(id=aid)
    teacherdata.teacher_status=1
    teacherdata.save()
    return redirect('wadmin:teacherverification')
def teacher_reject(request,rid):
    teacherdata=tbl_teacher.objects.get(id=rid)
    teacherdata.teacher_status=2
    teacherdata.save()
    return redirect('wadmin:teacherverification')

def Exam(request):
    exam=tbl_exam.objects.all()
    batch=tbl_batch.objects.all()
    subject=tbl_subject.objects.all()
    if request.method=="POST":
        bth_id = tbl_batch.objects.get(id=request.POST.get("ddl_batch"))
        sub_id = tbl_subject.objects.get(id=request.POST.get("ddl_subject"))
        tbl_exam.objects.create(exam_date=request.POST.get("txt_date"),batchid=bth_id,subjectid=sub_id)
        return redirect("wadmin:exam")
    else:
         return render(request, "Admin/Exam.html", {
              "exam": exam,
              "batch": batch,
              "subject": subject,
          })
    
def delete_exam(request,id):
     tbl_exam.objects.get(id=id).delete()
     return redirect("wadmin:exam")

def start_exam(request,stid):
     exam=tbl_exam.objects.get(id=stid)
     exam.exam_status=1
     exam.save()
     return redirect("wadmin:exam")
def end_exam(request,endid):
     exam=tbl_exam.objects.get(id=endid)
     exam.exam_status=2
     exam.save()
     return redirect("wadmin:exam")
     

           
    
         
    
def logout(request):
    print('Logout')
    if 'aid' in request.session:
        del request.session['aid']
        return redirect('wguest:login')
    else:
        return redirect('wguest:login')
    
def Viewreview(request):
    userdata=tbl_student.objects.all()
    userreview=tbl_review.objects.all()
    return render(request,"Admin/Viewreview.html",{'studentreview':userreview})