from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout',views.logout , name= 'logout'),
    path('add-driver/', views.add_driver, name='add_driver'),
    path('enter-travel/', views.enter_travel, name='enter_travel'),
    path('update-travel/<str:pk>/',views.update_travel,name='update_travel'),
    path('home-page/', views.home_page, name='home_page'),
    path('report-page/', views.report_page, name='report_page'),
    path('add-person/', views.add_person, name='add_person'),
]