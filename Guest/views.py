from django.shortcuts import render,redirect

from Admin.models import *
from Guest.models import *
from Teacher.models import *

# Create your views here.
def Teacherregisteration(request):
    district = tbl_district.objects.all()
    batch = tbl_batch.objects.all()
    teacherdata = tbl_teacher.objects.all()
    if request.method=="POST":
         place_id=tbl_place.objects.get(id=request.POST.get("txt_place"))
         subject_id=tbl_subject.objects.get(id=request.POST.get("txt_subject"))
         tbl_teacher.objects.create(teacher_name=request.POST.get("txt_name"),
                                            teacher_contact=request.POST.get("txt_contact"),
                                            teacher_email=request.POST.get("txt_email"),
                                            teacher_password=request.POST.get("txt_password"),
                                            teacher_address=request.POST.get("txt_address"),
                                            teacher_photo=request.FILES.get("txt_photo"),
                                            teacher_proof=request.FILES.get("txt_proof"),
                                            teacher_gender=request.POST.get("gender"),
                                            place_id=place_id,
                                            subject_id=subject_id,
                                            )
         return redirect('wguest:teacherregisteration')
    else:
         return render(request,"Guest/Teacherregisteration.html/",{"District":district ,"teacherdata":teacherdata,"batch":batch })
    
def ajax_place(request):
    distid=tbl_district.objects.get(id=request.GET.get("disid"))
    place_data=tbl_place.objects.filter(district_id=distid)
    return render(request,"Guest/AjaxPlace.html",{'Place':place_data})

def ajax_subject(request):
    bthid=tbl_batch.objects.get(id=request.GET.get("bthid"))
    subject_data=tbl_subject.objects.filter(batch_id=bthid)
    return render(request,"Guest/AjaxSubject.html",{'Subject':subject_data})

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')
        tcount= tbl_teacher.objects.filter(teacher_email = email , teacher_password = password, teacher_status= 1).count()
        acount = tbl_admin.objects.filter(admin_email = email, admin_password = password).count()
        scount = tbl_student.objects.filter(student_email = email, student_password = password).count()


        if acount > 0:
            admin = tbl_admin.objects.get(admin_email = email, admin_password = password)
            request.session["aid"] = admin.id
            return redirect('wadmin:homepage')
        
        elif tcount > 0:
            teacher = tbl_teacher.objects.get(teacher_email = email, teacher_password = password)
            request.session["tid"] = teacher.id
            return redirect('wteacher:homepage')
        
        elif scount > 0:
            student = tbl_student.objects.get(student_email = email, student_password = password)
            request.session["sid"] = student.id
            return redirect('wstudent:homepage')
        else:
            error_message = "Invalid username or password"
            return render(request,'Guest/Login.html',{'msg':error_message})
    else:
        return render(request,'Guest/Login.html')
    
def Index(request):
    if request.method=="POST":
         return render(request,"Guest/index.html")
    else:
         return render(request,"Guest/index.html")