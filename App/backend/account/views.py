import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from profiles.models import *
from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request,username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render (request, "account/login.html", {"error":"Usename or Password Incorrect"})
    else:
        return render(request, "account/login.html")


def user_register(request):
    if request.method == "POST":
        name = request.POST["name"]
        department = request.POST["department"]
        year = request.POST["year"]
        id_number = request.POST["id_number"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        role = request.POST["role"]
        selected_courses = request.POST.getlist('courses')  # Capture the selected courses

        # Validate password match
        if password != repassword:
             return render (request, "account/register.html", {"error": "Passwords do not match."})

        # Validate username length
        if len(username) <= 5:
            return render (request, "account/register.html", {"error": "Username must be longer than 5 characters."})
        
        # Validate password length
        if len(password) <= 8:
            return render (request, "account/register.html", {"error": "Password must be longer than 8 characters."})

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            return render (request, "account/register.html", {"error": "Email already in use."})
        
        if User.objects.filter(username=username).exists():
            return render (request, "account/register.html", {"error": "Username already in use."})

        # Create user based on the role
        if role == 'admin':
            user = User.objects.create_user(username=username, email=email, password=password, is_superuser=True, is_staff=True)
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            group = Group.objects.get(name=role)
            user.groups.add(group)
            if role == 'student':
                student = Student.create(user, id_number, name, department, year=year, courses=selected_courses)
                student.save()
            elif role == 'teacher':
                teacher = Instructor.create(user=user, id_number=id_number, name=name, department=department, courses=selected_courses)
                teacher.save()

        user.save()
        login(request, user)  # Log the user in after registering
        return redirect("index")  # Redirect to the homepage
    else:
        return render(request, "account/register.html")
    
def user_logout(request):
    logout(request)
    return redirect("user_login")

def users(request):
    return render(request, 'pages/users.html', {'active_page': 'users'})


