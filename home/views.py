from multiprocessing import context
from django.shortcuts import render,HttpResponse
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
   return render(request,'contact.html')

# Create your views here.
