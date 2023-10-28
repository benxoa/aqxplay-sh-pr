from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as authlogin
from django.contrib.auth.decorators import login_required
from .models.publish import Publish


# Create your views here.

def home(request):
    data = Publish.objects.all()
    context = {'x':data}
    return render(request, 'home.html',context)

@login_required(login_url="/login")
def publish(request):
    if request.method == "POST":
        data = request.POST.get
        title= data('title')
       
        image = request.FILES.get('image')

        Publish.objects.create(
            title = title,
            
            image = image
        )

        return redirect(publish)


    return render(request, 'publish.html')

def signup(request):
    if request.method == "POST":
        data = request.POST.get
        username = data('username')
        email = data('email')
        pass1 = data('password')
        pass2 = data('password2')

        user  = User.objects.filter(username = username) or User.objects.filter(email = email)
        if user.exists():
            messages.info(request, " Username or Email Already Exits!")
            return redirect(signup)
        if pass1 != pass2:
            messages.info(request, " Password does'nt match!")
            return redirect(signup)
        
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(pass1)
        user.save()
        return redirect(login)
    

    return render(request, 'signup.html')

def login(request):
    if request.method== "POST":
        data = request.POST.get
        username = data('username')
        password = data('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "User does'nt Exits!")
            return redirect(login)
        else:
            authlogin(request, user)
            return redirect(publish)


        
    return render(request, 'login.html')