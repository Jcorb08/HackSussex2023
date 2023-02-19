from django.db import models
from .equipment import standard_equipment
from .buff import standard_buff
from .shark import shark


# Create your models here.
class attack_action(models.Model):
    equipment = models.CharField(max_length=30)
    buff = models.CharField(max_length=30)
    shark = models.CharField(max_length=30)
