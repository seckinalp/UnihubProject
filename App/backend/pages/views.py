from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import Group


def isAdmin(user):
    return user.is_superuser
    
# Create your vie1ws here.
def user_index(request):
    return render(request, 'pages/user-index.html', {'active_page': 'user-index'})

def index(request):
    return render(request, 'pages/index.html', {'active_page': 'index'})

def admin_index(request):
    return render(request, 'pages/admin-index.html', {'active_page': 'admin-index'})

def teacher_index(request):
    return render(request, 'pages/teacher-index.html', {'active_page': 'teacher-index'})

def analysis(request):
    if not request.user.is_superuser:
        return render(request, 'pages/analysis.html', {'active_page': 'analysis'})
    else:
        return redirect("/")
    

def assessments(request):
    return render(request, 'pages/assessments.html', {'active_page': 'assessments'})

def chat(request):
    return render(request, 'pages/chat.html', {'active_page': 'chat'})

def events(request):
    return render(request, 'pages/events.html', {'active_page': 'events'})

def grades(request):
    return render(request, 'pages/grades.html', {'active_page': 'grades'})

def notifications(request):
    return render(request, 'pages/notifications.html', {'active_page': 'notifications'})

def portfolio(request):
    return render(request, 'pages/portfolio.html', {'active_page': 'portfolio'})

def profile(request):
    return render(request, 'pages/profile.html', {'active_page': 'profile'})

def report(request):
    return render(request, 'reports/submit_report.html', {'active_page': 'report'})

def reports(request):
    return render(request, 'reports/view_report.html', {'active_page': 'reports'})


new_group, created = Group.objects.get_or_create(name='student')
new_group, created = Group.objects.get_or_create(name='teacher')

def assessments_teacher(request):
    return render(request, 'pages/assessments_teacher.html', {'active_page': 'assessments_teacher'})

def chat_teacher(request):
    return render(request, 'pages/chat_teacher.html', {'active_page': 'chat_teacher'})

def events_teacher(request):
    return render(request, 'pages/events_teacher.html', {'active_page': 'events_teacher'})

def events_student(request):
    return render(request, 'pages/events_student.html', {'active_page': 'events_student'})

def events_teacher_add(request):
    return render(request, 'pages/event_create.html', {'active_page': 'events_teacher/add'})

def events_student_add(request):
    return render(request, 'pages/event_create.html', {'active_page': 'events_student/add'})


def grades_teacher(request):
    return render(request, 'pages/grades_teacher.html', {'active_page': 'grades_teacher'})

def notifications_teacher(request):
    return render(request, 'pages/notifications_teacher.html', {'active_page': 'notifications_teacher'})

def profile_teacher(request):
    return render(request, 'pages/profile_teacher.html', {'active_page': 'profile_teacher'})

def report_teacher(request):
    return render(request, 'pages/report_teacher.html', {'active_page': 'report_teacher'})

def question_teacher(request):
    return render(request, 'pages/question_teacher.html', {'active_page': 'question_teacher'})