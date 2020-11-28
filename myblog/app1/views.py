from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("start a first page")

def customer(request):
    return HttpResponse("start a first page")

def detail(request,driver):
    return HttpResponse("this is a customer page %s"% driver)