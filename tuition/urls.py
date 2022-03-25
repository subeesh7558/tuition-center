"""tuition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base_app import views
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Staff_index$', views.Staff_index, name='Staff_index'),
    re_path(r'^Staff_leave/$', views.Staff_leave, name='Staff_leave'),
    re_path(r'^Staff_Student_det/$', views.Staff_Student_det, name='Staff_Student_det'),
    re_path(r'^Staff_apply_leave/$', views.Staff_apply_leave, name='Staff_apply_leave'),
    re_path(r'^Staff_Req_leave/$', views.Staff_Req_leave, name='Staff_Req_leave'),
    re_path(r'^Staff_studentsleave_table/$', views.Staff_studentsleave_table, name='Staff_studentsleave_table'),
    re_path(r'^Staff_current_students/$', views.Staff_current_students, name='Staff_current_students'),
    re_path(r'^Staff_previous_students/$', views.Staff_previous_students, name='Staff_previous_students'),

    re_path(r'^Account_Student_det/$', views.Account_Student_det, name='Account_Student_det'),
    re_path(r'^Account_previous_students/$', views.Account_previous_students, name='Account_previous_students'),

    re_path(r'^Staff_progress_report/$', views.Staff_progress_report, name='Staff_progress_report'),
    re_path(r'^Staff_progress_report_add/$', views.Staff_progress_report_add, name='Staff_progress_report_add'),
    re_path(r'^Staff_student_dashboard/(?P<id>\d+)/$', views.Staff_student_dashboard, name='Staff_student_dashboard'),
    re_path(r'^Staff_previous_student_dashboard/(?P<id>\d+)/$', views.Staff_previous_student_dashboard, name='Staff_previous_student_dashboard'),
    re_path(r'^Staff_progress_report_show/$', views.Staff_progress_report_show, name='Staff_progress_report_show'),
    re_path(r'^Staff_rejected_leave/(?P<id>\d+)/$', views.Staff_rejected_leave, name='Staff_rejected_leave'),
    re_path(r'^Staff_accepted_leave/(?P<id>\d+)/$', views.Staff_accepted_leave, name='Staff_accepted_leave'),
    re_path(r'^Staff_accepted_leave/(?P<id>\d+)/$', views.Staff_accepted_leave, name='Staff_accepted_leave'),

    re_path(r'^MAN_subjects/$', views.MAN_subjects, name='MAN_subjects'),
    re_path(r'^MAN_Updatesubject/(?P<id>\d+)/$', views.MAN_Updatesubject, name='MAN_Updatesubject'),
    re_path(r'^MAN_Viewsubject/$', views.MAN_Viewsubject, name='MAN_Viewsubject'),
    re_path(r'^MAN_subjectupdate/(?P<id>\d+)/$', views.MAN_subjectupdate, name='MAN_subjectupdate'),
    re_path(r'^MAN_subject_delete/(?P<id>\d+)/$', views.MAN_subject_delete, name='MAN_subject_delete'),
    





]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)