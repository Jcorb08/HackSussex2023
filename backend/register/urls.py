from django.urls import path
from .views import buff
from .views import register

urlpatterns = [
    path('', register.index, name='index'),
    path('new_user/', register.first_time_register, name = "first_time_register"),
    path('reset_registered_user/', register.reset_registered_user, name = 'reset_registered_user'),
    path('initial_standard_buff_table/', buff.initial_standard_buff_table, name = 'initial_standard_buff_table')

]