from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user/', views.first_time_register, name = "first_time_register"),
    path('reset_registered_user/', views.reset_registered_user, name = 'reset_registered_user'),
    path('initial_standard_equipment_table', views.initial_standard_equipment_table, name = 'initial_standard_equipment_table')

]