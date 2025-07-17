# models.py in your Django app directory

from django.db import models

class Document(models.Model):
    COURSE_CHOICES = [
        ('CS101', 'CS101'),
        ('CS102', 'CS102'),
        ('HUM112', 'HUM112'),
        ('CS223', 'CS223'),
        ('CS224', 'CS224'),
    ]

    title = models.CharField(max_length=200,null=True, default=None)
    content = models.TextField(null=True, default=None)
    document_file = models.FileField(upload_to='documents/',null=True, default=None)
    related_course = models.CharField(max_length=6, choices=COURSE_CHOICES, default='not selected',null=True)

    def __str__(self):
        return self.title

# forms.py in your Django app directory

from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'content', 'document_file',  'related_course')
