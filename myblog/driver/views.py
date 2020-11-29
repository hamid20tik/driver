from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add_driver(request):
    return HttpResponse("<h1>add driver</h1> ")

def end_travel(request):
    return HttpResponse("<h1>End travel </h1>")

def enter_travel(request):
    return HttpResponse("<h1>enter travel </h1>")

def home_page(request):
    return HttpResponse("<h1>index homepage </h1>")

def login_page(request):
    return HttpResponse("<h1>login </h1>")

def report_page(request):
    return HttpResponse("<h1>report travel </h1>")
