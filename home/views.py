from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse("this is my home page(/)")
def about(request):
    return HttpResponse("this is my about page(/about)")
def projects(request):
    return HttpResponse("this is my projects page(/projects)")
def contact(request):
    return HttpResponse("this is my contact page(/contact)")

# Create your views here.
