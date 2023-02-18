from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user/', views.first_time_register, name = "first_time_register"),
    # path('')

]