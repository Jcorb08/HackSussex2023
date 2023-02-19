from django.contrib import admin
from .models.registered_user import registered_user
from .models.shark import shark
from .models.buff import standard_buff, available_buff
from .models.equipment import standard_equipment, available_equipment


# Register your models here.

admin.site.register(registered_user)
admin.site.register(shark)
admin.site.register(standard_buff)
admin.site.register(available_buff)
admin.site.register(standard_equipment)
admin.site.register(available_equipment)