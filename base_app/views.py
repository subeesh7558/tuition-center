from datetime import date, datetime
import imp
from django.shortcuts import render,redirect
from base_app.models import *
import os
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.

def login(request):
    
    des = designation.objects.get(designation='staff')
    des2 = designation.objects.get(designation='account')
    des3 = designation.objects.get(designation='manager')
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['prid'] = member.id
            request.session['usernametrns'] = member.designation_id
           
            if request.session.has_key('prid'):
                prid = request.session['prid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=prid)
            return render(request, 'Staff_index.html', {'pro':pro})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des2.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['accid'] = member.id
           
            if request.session.has_key('accid'):
                accid = request.session['accid']
            else:
                variable = "dummy"
            acco = user_registration.objects.filter(id=accid)
            return render(request, 'Acc_index.html', {'acco':acco})
        
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des3.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['manid'] = member.id
           
            if request.session.has_key('manid'):
                manid = request.session['manid']
            else:
                variable = "dummy"
            mani = user_registration.objects.filter(id=manid)
            return render(request, 'MAN_index.html', {'mani':mani})
    return render(request,'login.html')


def Staff_index(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
     return render(request, 'Staff_index.html',{'pro':pro})




def Staff_leave(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
     return render(request, 'Staff_leave.html',{'pro':pro})

def Staff_Student_det(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
     return render(request, 'Staff_Student_det.html',{'pro':pro})

def Staff_apply_leave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        pro2 = user_registration.objects.get(id=prid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user = pro2
            mem.designation_id=usernametrns
            mem.status = "pending"
            mem.save()
    return render(request, 'Staff_apply_leave.html',{'pro':pro})

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
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
     des = designation.objects.get(designation='student')
     cs = user_registration.objects.filter(designation_id=des).filter(status='active') .all().order_by('-id')
     cs = leave.objects.filter(designation_id=des.id).all().order_by('-id')
     return render(request, 'Staff_studentsleave_table.html',{'cs': cs,'pro':pro})


def Staff_current_students(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation='student')
        cs = user_registration.objects.filter(designation_id=des).filter(status='active') .all().order_by('-id')
    
     return render(request, 'Staff_current_students.html',{'cs': cs,'pro':pro})

def Staff_student_dashboard(request,id):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        csd=user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'Staff_student_dashboard.html',{'csd':csd,'pro':pro ,'labels': labels,'data': data})


def Staff_previous_students(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation='student')
        ps = user_registration.objects.filter(designation_id=des).filter(status='resigned') .all().order_by('-id')
        return render(request, 'Staff_previous_students.html',{'ps': ps,'pro':pro})

def Staff_previous_student_dashboard(request,id):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        psd=user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'Staff_previous_student_dashboard.html',{'psd':psd,'pro':pro,'labels': labels,'data': data})






def Staff_progress_det(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
     return render(request, 'Staff_progress_det.html',{'pro':pro})



def Staff_progress_report(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        desi = designation.objects.get(designation='student')
        sps = user_registration.objects.filter(designation_id=desi).filter(status='active') .all()
        sub = subject.objects.all()
        
        return render(request, 'Staff_progress_report.html',{'desi':desi,'sps': sps,'pro':pro,'sub':sub})
    
def Staff_progress_report_add(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            fn1 = request.POST['sname']
            fn2 = request.POST['ssubject']
            fn3 = request.POST['smark']
            fn4 = request.POST['sdate']
            
            
            students = user_registration.objects.get(fullname=fn1)
            su=subject.objects.get(subject=fn2)
            new2 = progressreport(user=students, subject=su, mark=fn3, date=fn4)
            new2.save()
           
        return redirect('Staff_progress_report')
 
    



def Staff_progress_report_show(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        pr=progressreport.objects.all()
        desi = designation.objects.get(designation='student')
        sps = user_registration.objects.filter(designation_id=desi).filter(status='active') .all()
        
        return render(request, 'Staff_progresss_report.html',{'pr':pr,'sps':sps,'pro':pro})


def Staff_progress_report_table(request,id):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        prog=user_registration.objects.filter(id=id)
        report=progressreport.objects.filter(id=id)
        return render(request, 'Staff_progress_report_table.html',{'prog':prog,'report':report,'pro':pro})



def Staff_rejected_leave(request,id):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            staff_reason=request.POST.get('reply')
            pro_sts = leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,status ='Rejected')
     return redirect('Staff_studentsleave_table')
   


def Staff_accepted_leave(request,id):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
    
        al = leave.objects.filter(id=id).update(status ='Approved')
       
            
        
     return redirect('Staff_studentsleave_table')


def MAN_index(request):
    if 'manid' in request.session:
        if request.session.has_key('manid'):
                manid = request.session['manid']
        else:
            variable = "dummy"
        mani = user_registration.objects.filter(id=manid)
    return render(request, 'MAN_index.html', {'mani':mani})

def MAN_subjects(request):
    if 'manid' in request.session:
        if request.session.has_key('manid'):
                manid = request.session['manid']
        else:
            variable = "dummy"
        mani = user_registration.objects.filter(id=manid)
    return render(request, 'MAN_subjects.html', {'mani':mani})


def MAN_Viewsubject(request):
    if 'manid' in request.session:
        if request.session.has_key('manid'):
                manid = request.session['manid']
        else:
            variable = "dummy"
    mani = user_registration.objects.filter(id=manid)
    sub=subject.objects.all()
    return render(request, 'MAN_Viewsubject.html',{'sub':sub,'mani':mani})


def MAN_Updatesubject(request,id):
    if 'manid' in request.session:
        if request.session.has_key('manid'):
                manid = request.session['manid']
        else:
            variable = "dummy"
        mani = user_registration.objects.filter(id=manid)
        sub=subject.objects.get(id=id)
        batches=batch.objects.all()
        return render(request, 'MAN_Updatesubject.html',{'sub':sub,'batches':batches,'mani':mani})

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






def Account_Student_det(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
    return render(request, 'Account_Student_det.html',{'acco':acco})

def Account_previous_students(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
    des = designation.objects.get(designation='student')
    aps = user_registration.objects.filter(status ="resigned" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request, 'Account_previous_students.html',{'aps': aps,'pay':pay,'acco':acco})

def Acc_index(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
    return render(request, 'Acc_index.html',{'acco':acco})


def Acc_Current_Student_det(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
    return render(request, 'Acc_Current_Student_det.html',{'acco':acco})




def Acc_current_students(request):
     if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
       
        des = designation.objects.get(designation='student')
        acs = user_registration.objects.filter(designation_id=des).filter(status='active') .all().order_by('-id')
        time = datetime.now()
        pay = payment.objects.all().order_by('-id')
     return render(request, 'Acc_current_students.html',{'acco':acco,'acs':acs,'time':time,'pay':pay})






def Acc_current_students_payment(request,id):
     if 'accid' in request.session:
        if request.session.has_key('accid'):
                accid = request.session['accid']
        else:
            variable = "dummy"
        acco = user_registration.objects.filter(id=accid)
        
        if request.method == 'POST':
            payuser=user_registration.objects.get(id=id)
            pay=payment()
            pay.date = datetime.now()
            pay.payment = request.POST['p']
            pay.user = payuser
            pay.save()
            return redirect('Acc_current_students')

            
            
        
     
