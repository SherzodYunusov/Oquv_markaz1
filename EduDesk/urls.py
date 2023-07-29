"""
URL configuration for EduDesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurs/', KursApiView.as_view()),
    path('ustoz/', UstozApiView.as_view()),
    path('xona/', XonaApiView.as_view()),
    path('oquvchi/', OquvchiApiView.as_view()),
    path('guruh/', GuruhApiView.as_view()),
    path('tolov/', TolovApiView.as_view()),
    path('davomat/', DavomatApiView.as_view()),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schames"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schames")),
    path('redocs/', SpectacularRedocView.as_view(url_name="schames")),
]
