from django.db import models
from instructor.models import Assessment, Grade, Attendance
from courses.models import Course

class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='studentuser')
    id_number = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    assesments = models.ManyToManyField(Assessment, blank=True)
    courses = models.JSONField(blank=True, null=True, default=None)    
    grades = models.ManyToManyField(Grade, blank=True)
    attendance = models.ManyToManyField(Attendance, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.id_number})"
    
    
    @classmethod
    def create(cls, user, id_number, name, department, year, courses):
        return cls.objects.create(user=user, id_number=id_number, name=name, department=department,year=year, courses=courses)
    
    
class Instructor(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='instructoruser')
    id_number = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    courses = models.JSONField(blank=True,  null=True, default=None)    
    
    def __str__(self):
        return f"{self.name} ({self.id_number})"
    
    @classmethod
    def create(cls, user, id_number, name, department,courses):
        return cls.objects.create(user=user, id_number=id_number, name=name, department=department, courses=courses)