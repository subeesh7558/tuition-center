from django.shortcuts import render
from base_app.models import *
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
    return render(request, 'Staff_studentsleave_table.html')