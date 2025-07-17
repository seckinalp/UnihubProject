from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

class EmailUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass  

class CustomEmailChangeForm(PasswordChangeForm):
    pass  