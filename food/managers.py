from django.db import models

class ActiveManager(models.Manager):
    def active_food(self):
        return self.filter(is_active=True)
    
class AvailableManager(models.Manager):
    def available_food(self):
        return self.filter(is_avaliable=True)
