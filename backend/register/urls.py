from django.urls import path

from .views import view_buff, view_shark
from .views import view_equirement
from .views import register

urlpatterns = [
    path('', register.index, name='index'),
    path('post_new_user/', register.first_time_register, name = "first_time_register"),
    path('reset_registered_user/', register.reset_registered_user, name = 'reset_registered_user'),
    path('initial_standard_buff_table/', view_buff.initial_standard_buff_table, name = 'initial_standard_buff_table'),
    path('initial_standard_equipments_table/', view_equirement.initial_standard_equipments_table, name = 'initial_standard_equipments_table'),
    path('get_all_standard_equipments/', view_equirement.get_all_standard_equipments, name = 'get_all_standard_equipments'),
    path('get_all_standard_buffs/', view_buff.get_all_standard_buffs, name = 'get_all_standard_buffs'),
    path('get_for_equipment_name/', view_equirement.get_for_equipment_name, name = 'get_for_equipment_name'),
    path('post_for_attack_shark/', view_shark.post_for_attack_shark, name = 'post_for_attack_shark'),
    path('get_initial_shark/', view_shark.get_initial_shark, name = 'get_initial_shark'),
    path('get_shark_hp/', view_shark.get_shark_hp, name = 'get_shark_hp'),

]