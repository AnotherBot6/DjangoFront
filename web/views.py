from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Log
from django.db.models import Max 
from django.db import connection
import json

def index(request):
    return render(request, 'web/index.html')

def log(request):
    latest_log = list(Log.objects.order_by('date').values())
    return JsonResponse(latest_log,safe=False)

def obtener_promedio():
    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(points) FROM web_log")
        resultado = cursor.fetchone()
        promedio = resultado[0] if resultado else None
    return promedio

def chart(request):
    maxp = Log.objects.all().aggregate(Max('points'))
    pointList = Log.objects.all().order_by('date')
    promedio = obtener_promedio()
    ctx = {'maxp': maxp["points__max"], 'pointList': pointList,"promedio": promedio}
    return render(request, 'web/chart.html',ctx)






