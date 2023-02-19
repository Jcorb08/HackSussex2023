from django.urls import path

from .views import view_buff
from .views import view_equirement
from .views import register

urlpatterns = [
    path('', register.index, name='index'),
    path('post_new_user/', register.first_time_register, name = "first_time_register"),
    path('reset_registered_user/', register.reset_registered_user, name = 'reset_registered_user'),
    path('initial_standard_buff_table/', view_buff.initial_standard_buff_table, name = 'initial_standard_buff_table'),
    path('initial_standard_equipments_table/', view_equirement.initial_standard_equipments_table, name = 'initial_standard_equipments_table'),
    path('get_all_standard_equipments/', view_equirement.get_all_standard_equipments, name = 'get_all_standard_equipments'),
    path('post_for_equipment_card', view_equirement.post_for_equipment_card, name = 'post_for_equipment_card')

]