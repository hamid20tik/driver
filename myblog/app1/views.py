from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>start a first page </h1>")

def customer(request):
    return HttpResponse("<h1>customers</h1>")

def detail(request):
    return HttpResponse("<h1>details</h1> ")

def safar(request):
    return HttpResponse("<h1>this is a safar page </h1>")

def insertsafar(request):
    return HttpResponse("<h1>this is a insert safar page </h1>")