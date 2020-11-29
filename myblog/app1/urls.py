from django.urls import path
from . import views

urlpatterns = [
    path('', views.safar, name = 'safarpage'),
    path('insert',views.insertsafar,name = "insertsafar"),
]