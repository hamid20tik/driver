from django.db import models
from django.utils import timezone
# Create your models here.

class driver(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    codemeli = models.BigIntegerField(max_length=15)
    phone = models.BigIntegerField(max_length=20)
    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.family, self.codemeli , self.phone)
    


class car(models.Model):
    car_name = models.CharField(max_length=20)
    car_model = models.CharField(max_length=4)
    car_pelak = models.CharField(max_length=8)
    def __str__(self):
        return '{} {} {}'.format(self.car_name , self.car_pelak , self.car_model)

class person(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    person_code = models.IntegerField(max_length=8)
    def __str__(self):
        return '{} {} {}'.format(self.name , self.family , self.person_code)

class safar(models.Model):
    driver = models.ForeignKey(driver , on_delete=models.CASCADE)
    car = models.ForeignKey(car , on_delete=models.CASCADE)
    person = models.ForeignKey(person,on_delete=models.CASCADE)
    mamoriat = models.CharField(max_length=50)
    maghsad = models.CharField(max_length= 300)
    mabda = models.CharField(max_length=300)
    datetime_start = models.DateTimeField(default=timezone.now)
    datetime_stop = models.DateTimeField(default=timezone.now)
    datetime_def = models.DateTimeField(default=timezone.now)
    datetime_now = models.DateTimeField(default=timezone.now)
    # def create(self):
    #     self.save()
    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(self.driver , self.car , self.person ,
         self.mamoriat,self.maghsad , self.mabda , self.datetime_start , self.datetime_stop , self.datetime_def , self.datetime_now)
#  

    