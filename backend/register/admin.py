from django.contrib import admin
from .models.user import registered_user
# Register your models here.

admin.site.register(registered_user)