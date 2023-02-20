"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from blog_app.views import home,about,suma,factorial,promedio,geo,ejercicio,ejer6,ejer7,ejer8,ejer9,ejer10,ejer11,ejer12,ejer13,ejer14,ejer15

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("suma/", suma, name="suma"),
    path("factorial/", factorial, name="factorial"),
    path("promedio/", promedio, name="promedio"),
    path("geo/", geo, name="geo"),
    path("ejercicio/", ejercicio, name="ejercicio5"),
    path("ejer6/", ejer6, name="ejer6"),
    path("ejer7/", ejer7, name="ejer7"),
    path("ejer8/", ejer8, name="ejer8"),
    path("ejer9/", ejer9, name="ejer9"),
    path("ejer10/", ejer10, name="ejer10"),
    path("ejer11/", ejer11, name="ejer11"),
    path("ejer12/", ejer12, name="ejer12"),
    path("ejer13/", ejer13, name="ejer13"),
    path("ejer14/", ejer14, name="ejer14"),
    path("ejer15/", ejer15, name="ejer15"),



    ]
