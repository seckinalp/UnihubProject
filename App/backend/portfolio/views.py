# views.py in your Django app directory

from django.shortcuts import render, redirect
from .models import Document, DocumentForm


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_documents')
    else:
        form = DocumentForm()
    return render(request, 'document_upload.html', {'form': form})

# views.py

def list_documents(request):
    related_course = request.GET.get('related_course', '')
    if related_course:
        documents = Document.objects.filter(related_course=related_course)
    else:
        documents = Document.objects.all()
    return render(request, 'document_list.html', {
        'documents': documents,
        'selected_course': related_course,
        'courses': Document.COURSE_CHOICES  # Assuming COURSE_CHOICES is defined in your model
    })


# views.py in your Django app directory

from django.shortcuts import get_object_or_404, redirect

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('list_documents')

