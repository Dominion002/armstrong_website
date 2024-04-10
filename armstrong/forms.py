from typing import Any
from . models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    name = forms.CharField(max_length=100, required=False)
    class Meta:
        model = User    
        fields = ['username','email','password1','password1','phone_number', 'name'] 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.all().filter(email=email).exists():
            raise forms.ValidationError('Email alredy exists')
        return email
    
class Customerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',] 
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:  # If instance exists and has a primary key
            if email == instance.email:  # If email hasn't been changed
                return email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

class Detailsform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number','address'] 
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:  # If instance exists and has a primary key
            if phone_number == instance.phone_number:  # If phone number hasn't been changed
                return phone_number
        if Customer.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone number already exists')
        return phone_number
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address.strip() == '':
            return None  # If address is blank, return None to allow it to be saved as null
        return address
    