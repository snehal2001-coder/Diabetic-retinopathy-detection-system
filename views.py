# importing required packages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect
from urllib import request
from diab_retina_app.models import newuser
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from diab_retina_app import process





#logout page









@csrf_exempt
def display(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        response = process.process_img(img)
		
        return HttpResponse(response, status=200)
    
	
def about(request):
	return render(request,'about.html')



def user_login(request):
  
        if request.method== 'POST':
            try:
                Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
                print("Username=",Userdetailes)
                request.session['Username']=Userdetailes.Username
                messages.success(request,"successfully login")
                return redirect('display')
            except newuser.DoesNotExist as e:   
                messages.error(request,"Username/ Password Invalied...!")
        return render(request, 'user_login.html')


def user_register(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 !=pass2:
            messages.error(request,"password do not match")
            return redirect('user_register')
        newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
        messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
        return redirect('user_login')
    else:
        return render(request, 'user_register.html')
    

# def my_view(request):
#     # ...
#     img = "my_image.jpg"
#     result = process_img(img)
    
#     prediction = Prediction(result=result[0], accuracy=result[2])
#     prediction.save()

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('user_login')

