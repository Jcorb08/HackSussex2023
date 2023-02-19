from django.db import models

# Create your models here.
class shark(models.Model):
    attack = models.IntegerField()
    deffence = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    
    def __str__(self):
        return 'shark ' + str(self.pk)