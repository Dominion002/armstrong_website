from typing import Any
from . models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User    
        fields = ['username','email','password1','password1'] 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.all().filter(email=email).exists():
            raise forms.ValidationError('Email alredy exists')
        return email
    
