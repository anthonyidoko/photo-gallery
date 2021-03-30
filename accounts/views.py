from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        
        if user:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid user")
            return redirect('.')
    
    return render(request, "login.html") 

def logout_view(request):
    auth.logout(request)
    return redirect("/")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.info(request,"password does not match")
            return redirect('.')
        elif len(password1) < 6:
            messages.info(request, "password too short")
            return redirect('.')
        elif email == User.objects.filter(email=email):
            messages.info(request, "email unavailable")
            return redirect('.')
        elif username == User.objects.filter(username=username):
            messages.info(request, "username unavailable")
            return redirect('.')
        else:
            user = User.objects.create_user(username = username,first_name=first_name,last_name=last_name,email=email,password=password1)
            messages.info(request,"user has been created")
            return redirect("/accounts/login")

    return render(request,"signup.html")
