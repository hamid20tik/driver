from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import driver,person

from django.contrib.auth.decorators import login_required
from django.contrib import auth,messages
from django.utils import timezone
from .forms import safarform
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
            return redirect('add_driver')
        else:
            return render(request,'add_driver.html',{'error':'تمامی مقادیر را به درستی وارد کنید '})
    else:
        obj = driver.objects.all()
        return render(request, 'add_driver.html', {'rep_driver':obj})

@login_required
def update_travel(request,pk):
    obj = safar.objects.get(id=pk)
    form = safarform(instance=obj)
    if request.method == 'POST':
        form = safarform(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('report_page')
    context={'form': form,'rep':obj}
    return render(request, 'end_travel.html', context)

@login_required
def enter_travel(request):
    form = safarform()
    obj = safar.objects.all()
    objd = driver.objects.all()
    objp = person.objects.all()
    if request.method == 'POST':
        form = safarform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enter_travel')
        # if request.POST['driver'] and request.POST['person'] and request.POST['mamoriat'] and request.POST['maghsad'] and request.POST['mabda']:
        #
        #     saf = safar()
        #     saf.driver = request.POST.get('driver')
        #     saf.person = request.POST.get('person')
        #     saf.mamoriat = request.POST['mamoriat']
        #     saf.maghsad = request.POST['maghsad']
        #     saf.mabda = request.POST['mabda']
        #     saf.datetime_start = timezone.now
        #     saf.save()
        #     return redirect('enter_travel')
        # else:
        #     return render(request,'enter_travel.html',{'error':'تمامی مقادیر را به درستی وارد کنید '})
    return render(request, 'enter_travel.html',{'rep_travel':obj,'rep_dri':objd,'rep_per':objp,'form':form})
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
    result = safar.objects.all()
    return render(request,'report.html', {'rep_safar':result})
