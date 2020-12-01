from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,context
from .models import safar
# Create your views here.

def add_driver(request):
    return render(request,'add_driver.html')

def end_travel(request):
    return render(request,'end_travel.html')

def enter_travel(request):
    return render(request,'enter_travel.html')

def home_page(request):
    return render(request,'index.html')

def login_page(request):
    return render(request,'login.html')

def report_page(request):
    return render(request,'report.html')
