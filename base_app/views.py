from datetime import date
import imp
from django.shortcuts import render,redirect
from base_app.models import *
import os
# Create your views here.

def login(request):
    
    des = designation.objects.get(designation='staff')
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['prid'] = member.id
           
            if request.session.has_key('prid'):
                prid = request.session['prid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=prid)
            return render(request, 'Staff_index.html', {'pro':pro})
    return render(request,'login.html')


def Staff_index(request):
    return render(request, 'Staff_index.html')

def Staff_leave(request):
    return render(request, 'Staff_leave.html')

def Staff_Student_det(request):
    return render(request, 'Staff_Student_det.html')

def Staff_apply_leave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        pro2 = designation.objects.filter(id=prid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('pr_id')
            mem.designation_id = request.POST.get('sf_id')
            mem.status = "pending"
            mem.save()
    return render(request, 'Staff_apply_leave.html',{'pro':pro,'pro2':pro2})

def Staff_Req_leave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        var = leave.objects.filter(user_id=prid).order_by("-id")
    return render(request, 'Staff_Req_leave.html',{'pro':pro,'var':var})

# def Student_profiledash(request):
#     return render(request, 'Student_profiledash.html')


def Staff_studentsleave_table(request):
     des = designation.objects.get(designation='student')
     sl = leave.objects.filter(designation_id=des.id).all().order_by('-id')
     return render(request, 'Staff_studentsleave_table.html',{'sl': sl})


def Staff_current_students(request):
    des = designation.objects.get(designation='student')
    cs = user_registration.objects.filter(status='active') .all().order_by('-id')
    
    return render(request, 'Staff_current_students.html',{'cs': cs})

def Staff_student_dashboard(request,id):
    csd=user_registration.objects.filter(id=id)
    return render(request, 'Staff_student_dashboard.html',{'csd':csd})


def Staff_previous_students(request):
    des = designation.objects.get(designation='student')
    ps = user_registration.objects.filter(status='resigned') .all().order_by('-id')
    return render(request, 'Staff_previous_students.html',{'ps': ps})

def Staff_previous_student_dashboard(request,id):
    psd=user_registration.objects.filter(id=id)
    return render(request, 'Staff_previous_student_dashboard.html',{'psd':psd})


def Account_Student_det(request):
    return render(request, 'Account_Student_det.html')

def Account_previous_students(request):
    des = designation.objects.get(designation='student')
    aps = user_registration.objects.filter(status ="resigned" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request, 'Account_previous_students.html',{'aps': aps,'pay':pay})



def Staff_progress_report(request):
    desi = designation.objects.get(designation='student')
    sps = user_registration.objects.filter(status='active') .all()
    return render(request, 'Staff_progress_report.html',{'desi':desi,'sps': sps})

def Staff_progress_report_add(request):
    if request.method == 'POST':
        fn1 = request.POST['sname']
        fn2 = request.POST['ssubject']
        fn3 = request.POST['smark']
        fn4 = request.POST['sdate']
        
        
        students = user_registration.objects.get(fullname=fn1)
        
        new2 = progressreport(user=students, subject=fn2, mark=fn3, date=fn4)
        new2.save()
    return redirect('Staff_progress_report_show')
    



def Staff_progress_report_show(request):
    pr=progressreport.objects.all()
    sps = user_registration.objects.filter(status='active') .all()
    
    return render(request, 'Staff_progresss_report.html',{'pr':pr,'sps':sps})



def Staff_rejected_leave(request,id):
    if request.method == 'POST':
        staff_reason=request.POST.get('reply')
        pro_sts = leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,status ='Rejected')
        
       
    return redirect('Staff_studentsleave_table')


def Staff_accepted_leave(request,id):
    
    al = leave.objects.filter(id=id).update(status ='Approved')
        
       
    return redirect('Staff_studentsleave_table')


def MAN_subjects(request):
    return render(request, 'MAN_subjects.html')


def MAN_Viewsubject(request):
    sub=subject.objects.all()
    return render(request, 'MAN_Viewsubject.html',{'sub':sub})


def MAN_Updatesubject(request,id):
    sub=subject.objects.get(id=id)
    batches=batch.objects.all()
    return render(request, 'MAN_Updatesubject.html',{'sub':sub,'batches':batches})

def MAN_subjectupdate(request,id):
        
        if request.method == 'POST':
            subed = subject.objects.get(id=id)
            subed.subject = request.POST.get('subj')
            subed.rate = request.POST.get('srate')
            
    
       
            try:
                subed.logo = request.FILES['slogo']
            except:
                pass
            
            br_id = request.POST.get("subbatch")
            subed.batch_id = br_id
            subed.save()
            return redirect('MAN_Viewsubject')

def MAN_subject_delete(request, id):
    subed = subject.objects.get(id=id)
    
        
    subed.delete()
    return redirect('MAN_Viewsubject')

