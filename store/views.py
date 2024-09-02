from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from.models import Category,Product
from django.http import HttpResponse

# Create your views here.

def home(request):

   return render(request,'index.html')

def register(request):
   if request.method=="POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
               messages.info(request,"username already exists")
               return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request,"email already exists")
               return redirect('register')
            else :
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/')
   else :
            return render(request,'register.html')
def login(request):
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
          auth.login(request,user)
          return redirect('/')
      else:
           messages.info(request,"invalid login")
           return redirect('login')
   return render(request,'login.html')

def collection(request):
    category=Category.objects.filter(status=0)
    return render(request,'collection.html',{'category':category})

def product(request):
    product=Product.objects.filter(status=0)

    return render(request,'product.html',{'product':product})
