"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name="loginpage" ),
    path('login/auth', views.login, name="login"),
    path('lark/auth', views.lark_login, name ="lark_login"),
    path('logout/', views.logout, name="logout" ),
    path('', views.homePage, name="dashboard" ),
    path('about/', views.aboutPage ),
    path('settings/', views.settingsPage ),
    path('notifications/', views.notificationsPage ),
    path("__reload__/", include("django_browser_reload.urls")),
]
