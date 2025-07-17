#Unihub - Unihub - urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create-question/', views.create_question_view, name='create-question'),
    path('question-list/', views.question_list_view, name='question-list'),
    path('question-detail/<int:pk>/', views.question_detail_view, name='question-detail'),
    path('new-assessment/', views.new_assessment_view_1, name="new-assessment"),
    path('assessment-add-question/<int:pk>/', views.assessment_add_question_view, name="assessment-add-question"),
    path('assessment-list/', views.assessment_list_view, name='assessment-list'),
    path('assessment-detail/<int:pk>', views.assessment_detail_view, name='assessment-detail'),
    path('assessment-detail/<int:pk>/export/', views.export_assessment, name='export_assessment'),
    path('assessment-assign/<int:pk>', views.assign_assessment, name='assessment-assign'),
    path('student-assessment-list/', views.student_assessment_list, name="student-assessment-list"),
    path('student-assessment-list/<int:pk>/export', views.export_assessment_student, name='export_asessment_student'),
    path('grade/', views.grade, name='grade'),
    path('student-grades/', views.student_grades, name='student-grades'),
]
