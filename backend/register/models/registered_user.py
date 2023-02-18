from django.db import models

# Create your models here.
class registered_user(models.Model):
    user_name = models.CharField(max_length=30)
    IP_address = models.GenericIPAddressField()
    
    def __str__(self):
        return self.user_name