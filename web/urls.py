from django.urls import path, include
from  . import  views
from django.views.generic import TemplateView 

app_name = 'web'

urlpatterns = [
    
    path('', views.index, name = "index"),
    path('index',views.index, name = "index"),    
    path('chart',views.chart, name = "chart"),
    path('log',views.log, name = "log"), 
]