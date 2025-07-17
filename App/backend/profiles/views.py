from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.contrib import messages


@login_required
def update_student_profile(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])

    user = request.user
    new_email = request.POST.get('email')
    new_password = request.POST.get('password')
    new_password2 = request.POST.get('password2')

    if len(new_password) <= 8:
        return render (request, "editinstructor.html", {"error": "Password must be longer than 8 characters."})
    
    # Ensure that new passwords match
    if new_password and new_password == new_password2:
        # Update the password
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Keep the user logged in after password change
        messages.success(request, 'Password updated successfully.')

        if new_email:
            # Update the email if provided
            user.email = new_email
            user.save()
    else:
        # Handling cases where passwords do not match or no new password is provided
        return render (request, "editstudent.html", {"error": 'Passwords do not match.'})

    # Redirect to the profile page after update
    return redirect('showprofile')  # Ensure the redirect URL name matches your URL configuration


@login_required
def update_instructor_profile(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])

    user = request.user
    new_email = request.POST.get('email')
    new_password = request.POST.get('password')
    new_password2 = request.POST.get('password2')
     
    if len(new_password) <= 8:
        return render (request, "editinstructor.html", {"error": "Password must be longer than 8 characters."})

    if new_password and new_password == new_password2:
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Keep the user logged in after password change
        messages.success(request, 'Password updated successfully.')

        if new_email:
            user.email = new_email
            user.save()
        return redirect('showIns')
    else:
        return render (request, "editinstructor.html", {"error": 'Passwords do not match.'})  # Render the same template to show the form again

def show_student(request, student_id):
    profile = get_object_or_404(profile, pk=student_id)
    return render(request, 'showstudent.html', {'student': profile})

def show_instructor(request, student_id):
    profile = get_object_or_404(profile, pk=student_id)
    return render(request, 'showinstructor.html', {'instructor': profile})


def edit_loginedstudent(request):
    return render(request, 'editstudent.html', {'student': request.user})

def edit_loginedInstructor(request):
    return render(request, 'editinstructor.html', {'instructor': request.user})

def show_loginedstudent(request):
    user_profile = Student.objects.filter(user=request.user).first()
    
    # Check if a UserProfile instance exists for the user
    if user_profile is None:
        return HttpResponse("No user profile available for this user.", status=404)

    # Pass the UserProfile instance to the template instead of request.user
    return render(request, 'showstudent.html', {'student': user_profile})


def show_loginedInstructor(request):
    user_profile = Instructor.objects.filter(user=request.user).first()
    
    # Check if a UserProfile instance exists for the user
    if user_profile is None:
        return HttpResponse("No user profile available for this user.", status=404)

    # Pass the UserProfile instance to the template instead of request.user
    return render(request, 'showinstructor.html', {'instructor': user_profile})