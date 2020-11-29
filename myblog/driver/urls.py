from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('add-driver',views.add_driver),
    path('enter-travel',views.enter_travel),
    path('end-travel',views.end_travel),
    path('home-page',views.home_page),
    path('report-page',views.report_page),
]