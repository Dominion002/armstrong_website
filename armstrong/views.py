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
    user = request.user
    first_error = ("","")
    second_error = ("","")
    if request.method  == "POST":
        form =  Customerform(request.POST,instance=user)
        d_form = Detailsform(request.POST,instance=user.customer)
        if form.is_valid() and d_form.is_valid():
            form.save()
            d_form.save()
            messages.success(request,'Account was sucesfully updated')
            return redirect('settings') 
        else:
            if not form.is_valid():
                first_error = next((field, errors[0]) for field, errors in form.errors.items())
            elif not d_form.is_valid():
                second_error = next((field, errors[0]) for field, errors in d_form.errors.items())
           
        
    else:
        form =  Customerform(instance=user)
        d_form = Detailsform(instance=user.customer)
    context = { 'd_form':d_form, 'form':form, "error":first_error,"error2":second_error}
    return render(request,'profile.html',context)
# views.py

from django.http import JsonResponse

def check_armstrong(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data.get('number') 
        result = is_armstrong(int(number))
        if request.user.is_authenticated:
            if number != "":
                if result:
                    print("armstrong")
                    new_number = History.objects.create(user = request.user,number = number ,result=f"{number} is an armstrong number")
                    new_number.save()
                else:
                    print("not armstrong")
                    new_number = History.objects.create(user = request.user,number = number ,result=f"{number} is not an armstrong number")
                    new_number.save()
                     
               
                
            
          
        
        
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def check_armstrongRange(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        frome = data.get('frome')  
        to = data.get('to')
        result = armstrong_numbers_between(int(frome), int(to))
        print(result)
        if request.user.is_authenticated:
            if frome  != "" and to != "":
                if(len(result) > 0):
                    new_number = History.objects.create(user=request.user,from_number=frome,to_number=to,result=f"{len(result)} armstrong numbers found ,{result}")
                    new_number.save()
                else:
                    new_number = History.objects.create(user=request.user,from_number=frome,to_number=to,result=f"No armstrong numbers found ")
                    new_number.save()
                    
                
        
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
             user = userform.save()
             Customer.objects.create(
                user=user,
                phone_number=userform .cleaned_data.get('phone_number'),
                name=userform.cleaned_data.get('name')
            )
             usern  = userform.cleaned_data.get('username')
             messages.success(request,'Account was created for '+ usern)
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


def user_history(request):
    # Get the logged-in user's history
    user_history = History.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'history.html', {'user_history': user_history})