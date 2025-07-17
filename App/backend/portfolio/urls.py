# urls.py in your Django app directory

from django.urls import path
from .views import upload_document, list_documents, delete_document

urlpatterns = [
    path('documents/upload/', upload_document, name='upload_document'),
    path('documents/', list_documents, name='list_documents'),
    path('delete/<int:pk>/', delete_document, name='delete_document'),
]
