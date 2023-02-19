from django.db import models
from .registered_user import registered_user
from .shark import shark

# Create your models here.
class standard_equipment(models.Model):
    equipment_name = models.CharField(max_length=30)
    attack = models.IntegerField()
    deffence = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.equipment_name

class available_equipment(models.Model):
    standard_equipment_ID = models.ForeignKey(standard_equipment, on_delete = models.CASCADE)
    owner = models.ForeignKey(registered_user, on_delete = models.CASCADE)
    affect_on = models.ForeignKey(shark, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.standard_equipment_ID.equipment_name