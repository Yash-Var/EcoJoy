"""Rakathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include 
from django.shortcuts import render
from django.views.generic import TemplateView
from . import views , settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home , name = "home"),
    path('about/', views.about),
    path('shop/', views.shop),
    path('blog/', views.blog),
    path('portfolio/', views.portfolio),
    path('identifier/', views.identifier),
    path('identified/', views.identified),
    path('blog/<int:id>',views.blogpage, name='blogpost'),
    path('plant/<int:id>',views.plants, name='plants'),
    path('contact/', include('contact_queries.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
