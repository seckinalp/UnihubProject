from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_loginedstudent, name= 'showprofile'),
    path('showIns/', views.show_loginedInstructor, name= 'showIns'),
    path('show/<int:student_id>', views.show_student, name='showstudent'),
    path('show/<int:id_number>', views.show_instructor, name='showinstructor'),
    path('edit/', views.edit_loginedstudent, name= 'edit'),
    path('editIns/', views.edit_loginedInstructor, name = 'editIns'),
    path('update/', views.update_student_profile, name='update_profile'),
    path('updateIns/', views.update_instructor_profile, name='update_instructor')
]
