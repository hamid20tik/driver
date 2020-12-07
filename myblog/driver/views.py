from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import driver,person,safar
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from django.template import loader,context
from .models import safar
# Create your views here.
@login_required
def add_driver(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['fname'] and request.POST['codemeli'] and request.POST['phone'] and request.POST['car_name'] and request.POST['car_model'] and request.POST['car_pelak']:
            dri = driver()
            dri.name= request.POST['name']
            dri.family = request.POST['fname']
            dri.codemeli = request.POST['codemeli']
            dri.phone = request.POST['phone']
            dri.car_name = request.POST['car_name']
            dri.car_model = request.POST['car_model']
            dri.car_pelak = request.POST['car_pelak']
            dri.save()
            return redirect('home_page')
        else:
            return render(request,'add_driver.html',{'error':'تمامی مقادیر را به درستی وارد کنید '})
    else:
        return render(request,'add_driver.html')
@login_required
def end_travel(request):
    return render(request,'end_travel.html')
@login_required
def enter_travel(request):
    return render(request, 'enter_travel.html')
@login_required
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است'})
    else:
        return render(request,'login.html')
@login_required
def logout(requset):
    if requset.method=='POST':
        auth.logout(requset)
        return redirect('login_page')

@login_required
def add_person(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['fname'] and request.POST['codeperson']:
            per = person()
            per.name=request.POST['name']
            per.family = request.POST['fname']
            per.person_code = request.POST['codeperson']
            per.save()
            return redirect('add_person')
        else:
            return render(request,'add_person.html',{'error':'تمامی مقادیر را به درستی وارد کنید '})
    else:
        obj = person.objects.all()
        return render(request,'add_person.html',{'rep_person':obj})


@login_required
def report_page(request):
    obj = safar.objects.all()
    return render(request,'report.html', {'rep_safar':obj})
