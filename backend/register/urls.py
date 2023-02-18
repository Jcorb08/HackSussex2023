from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user/', views.first_time_register, name = "register")
]