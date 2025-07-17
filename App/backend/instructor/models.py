from django.db import models
from courses.models import Course
    
class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    course = models.CharField(blank=True, null=True, default=None, max_length=255)
    value = models.IntegerField(default=0)    
    
    @classmethod
    def create(cls, description, course, value):
        return cls.objects.create(description=description, course=course, value=value)
    
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.CharField(blank=True, null=True, default=None, max_length=255)
    date = models.DateField(null=True)
    attended = models.BooleanField(default=False)
    
    @classmethod
    def create(cls, course, date, attended):
        return cls.objects.create(course=course, date=date, attended=attended)
    
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    prompt = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    category = models.JSONField(blank=True, null=True, default=None)
    difficulty = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.prompt)
    
    @classmethod
    def create(cls, prompt, answer, category, difficulty):
        return cls.objects.create(prompt=prompt, answer=answer, category=category, difficulty=difficulty)
    
class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.JSONField(blank=True, null=True, default=None)
    questions = models.ManyToManyField(Question)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_assigned = models.BooleanField(default=False)
    
    @classmethod
    def create(cls, name, course):
        return cls.objects.create(name=name, course=course)
    
    def update_assessment(self, questions=None, start_date=None, end_date=None):
        if questions:
            self.questions.add(*questions)
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date
        self.is_assigned = True
        self.save()
        
        
    

