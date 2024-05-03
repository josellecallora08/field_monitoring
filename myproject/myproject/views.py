# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password =password).first()
        if user:
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'loginPage')

def logout(request): 
    return redirect('loginpage')

# Pages


def homePage(request):
    stepcount = [
    { "y": 10560, "label":"Sunday" },
    { "y": 9060, "label":"Monday" },
    { "y": 6650, "label":"Tuesday" },
    { "y": 8305, "label":"Wednesday" },
    { "y": 8531, "label":"Thursday" },
    { "y": 10150, "label":"Friday" },
    { "y": 8921, "label":"Saturday" }
    ]
  
    return render(request, 'pages/index.html', { "stepcount": stepcount })    

def loginPage(request):
    return render(request, 'pages/login.html')

def aboutPage(request):
    return render(request, 'pages/about.html')

def settingsPage(request):
    return render(request, 'pages/settings.html')

def notificationsPage(request):
    return render(request, 'pages/notification.html')