# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    stepcount = [
    { "y": 10560, "label":"Sunday" },
    { "y": 9060, "label":"Monday" },
    { "y": 6650, "label":"Tuesday" },
    { "y": 8305, "label":"Wednesday" },
    { "y": 8531, "label":"Thursday" },
    { "y": 10150, "label":"Friday" },
    { "y": 8921, "label":"Saturday" }
    ]
  
    return render(request, 'index.html', { "stepcount": stepcount })    


def about(request):
    return render(request, 'about.html')

def settings(request):
    return render(request, 'settings.html')

def notifications(request):
    return render(request, 'notification.html')
