from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from .forms import *
from django import forms
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth import login
from . decorators import *
from . models import *
# Create your views here.
def index(request):
    return render(request,'index.html')  

def settings(request):
    return render(request,'profile.html')

# views.py

from django.http import JsonResponse

def check_armstrong(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data.get('number') 
        if request.user.is_authenticated:
            if number != "":
                new_number = History.objects.create(user = request.user,number = number)
                new_number.save()
            
          
        
        result = is_armstrong(int(number))
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def check_armstrongRange(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        frome = data.get('frome')  
        to = data.get('to')
        if request.user.is_authenticated:
            if frome and to != "":
                new_number = History.objects.create(user=request.user,from_number=frome,to_number=to)
                new_number.save()
        result = armstrong_numbers_between(int(frome), int(to))
        print(result)
        if result:
            return JsonResponse({'result': result})
        
            
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def is_armstrong(number):
    # Logic to check if the number is an Armstrong number
    total = 0
    num = number
    n = len(str(number))
    while num > 0:
        digit = num % 10
        total += digit ** n
        num //= 10
    return number == total


def armstrong_numbers_between(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

@unauthenticated_user
def register(request):
    errors =("","")
    userform = UserForm()    
    if request.method == "POST":
         userform = UserForm(request.POST)
         if userform.is_valid():
             userform.save()
             user  = userform.cleaned_data.get('username')
             messages.success(request,'Account was created for '+ user)
             return redirect("login")
         else:
             errors = next((name , error[0]) for name,error  in userform.errors.items())
             print(errors)  
    context = {"form":userform,'errors':errors}
    return render(request,'register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:     
            messages.info(request,"Username or Password is incorrect")
            return render(request,'login.html')
    return render(request,'login.html')

def logoutPage(request):
    
    logout(request)
    return redirect('login')

def send_feedback(request):
    if request.user.is_authenticated:
        name = request.user.username
        email = request.user.email
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
      
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(user=name, email=email, subject=subject, message=message)
        feedback.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)