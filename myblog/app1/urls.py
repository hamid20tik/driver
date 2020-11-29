from django.urls import path
from . import views

urlpatterns = [
    path('', views.safar),
    path('insert',views.insertsafar),
]