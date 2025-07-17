from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('index', views.home1),
    path('<course_name>', views.home2),
    path('category/<int:category_id>', views.getCoursesByID),
    path('category/<str:category_name>', views.getCoursesByCategory, name= 'courses_by_category'),
]
