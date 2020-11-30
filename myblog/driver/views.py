from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,context
from .models import safar
# Create your views here.

def add_driver(request):
    t = loader.get_template('driver/add_driver.html')
    context = {}
    return HttpResponse(t.render(context,request))

def end_travel(request):
    t = loader.get_template('driver/end_travel.html')
    context = {}
    return HttpResponse(t.render(context,request))

def enter_travel(request):
    t = loader.get_template('driver/enter_travel.html')
    context = {}
    return HttpResponse(t.render(context,request))

def home_page(request):
    t = loader.get_template('driver/index.html')
    context = {}
    return HttpResponse(t.render(context,request))
def login_page(request):
    t = loader.get_template('driver/login.html')
    context = {}
    return HttpResponse(t.render(context, request))
def report_page(request):
    t = loader.get_template('driver/report.html')
    context = {}
    return HttpResponse(t.render(context,request))
