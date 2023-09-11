from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('getdata/', views.getdata),
    path('mypage/', include('mypage.urls')),
]
