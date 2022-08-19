from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home import models
from home.models import Contact
def home(request):
   # return HttpResponse("this is my home page(/)")
   context={'name':'Prasant','course':'Django'}
   return render(request,'home.html',context)

def about(request):
    #return HttpResponse("this is my about page(/about)")
    
    return render(request,'about.html')

def projects(request):
    #return HttpResponse("this is my projects page(/projects)")
    return render(request,'projects.html')
def contact(request):
   # return HttpResponse("this is my contact page(/contact)")
   if request.method=="POST":
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       desc=request.POST['desc']
       ins=Contact(name=name,email=email,phone=phone,desc=desc)
       #print(name,email,phone,desc)
       ins.save()
       print("hello")
   return render(request,'contact.html')

# Create your views here.
