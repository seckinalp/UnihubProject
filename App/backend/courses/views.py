from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

data = {
    "cs100":"cs 100 kursu",
    "cs101":"cs 101 kursu",
    "cs102":"cs 102 kursu",
    "cs103":"cs 103 kursu",
}
def home1(request):
    return HttpResponse('kurs listesi')

def index(request):
    return render(request,'courses/index.html')


def home2(request,course_name):
    return HttpResponse(f'{course_name} details')

def getCoursesByCategory(request, category_name):
    try:
        text = data[category_name]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("wrong category")

def getCoursesByID(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("wrong category")
    redirect_text = category_list[category_id - 1 ]
    
    redirect_url = reverse('courses_by_category', args=[redirect_text])
    return HttpResponseRedirect(redirect_url)