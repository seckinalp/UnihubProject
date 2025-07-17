from django.urls import path
from .import views
from event.views import EventCreateView, EventListView, EventUpdateView, EventDeleteView
from account.views import user_login


urlpatterns = [
    path('', user_login , name = "login"),
    path('index/', views.index, name='index'),
    path('user-index', views.user_index),
    path('admin-index', views.admin_index),
    path('teacher-index', views.teacher_index),
    path('analysis', views.analysis),
    path('assessments', views.assessments),
    path('chat', views.chat),
    path('events', views.events),
    path('grades', views.grades),
    path('notifications', views.notifications),
    path('portfolio', views.portfolio),
    path('profile', views.profile),
    path('report', views.report),
    path('reports', views.reports),
    
    path('report_teacher', views.report_teacher),
    path('assessments_teacher', views.assessments_teacher),
    path('chat_teacher', views.chat_teacher),
    path('events_teacher', views.events_teacher, name='events_teacher'),
    path('events_student', views.events_student,name ='events_student'),
    path('events_teacher/add', EventCreateView.as_view()),
    path('events_student/add', EventCreateView.as_view()),

    path('grades_teacher', views.grades_teacher),
    path('notifications_teacher', views.notifications_teacher),
    path('profile_teacher', views.profile_teacher),
    path('question_teacher', views.question_teacher),

    path('events_teacher/<int:event_id>/', EventListView.event_detail, name='event_detail'),
    path('events_student/<int:event_id>/', EventListView.event_detail, name='event_detail'),
    path('events_teacher/all/', EventListView.all_events, name = 'all_student_events'),
    path('events_student/all/', EventListView.all_events, name = 'all_teacher_events'),

    path('events_teacher/<int:event_id>/edit/', EventUpdateView.edit_event, name='edit_event'),
    path('events_teacher/<int:event_id>/delete/', EventDeleteView.delete_event, name='delete_event'),

    path('events_student/<int:event_id>/edit/', EventUpdateView.edit_event, name='edit_event'),
    path('events_student/<int:event_id>/delete/', EventDeleteView.delete_event, name='delete_event'),
  
    
]
