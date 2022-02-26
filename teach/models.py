from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class Tenants(models.Model):

    CHOICES = (
        ('2 Br','Two bedroom'),
        ('3 Br','Three bedroom'),
        ('1 Br','One bedroom'),
        ('Bst','Bedsitter')

    )

    tname = models.CharField(max_length=30)
    tmarital_status = models.CharField(max_length=10)
    tdate_in = models.DateField()
    troom_type = models.CharField(max_length=300, choices=CHOICES)
    

    class Meta:
        verbose_name = ('ToDo')
        verbose_name_plural  = ("Todo")
    
    def __str__(self):
        return self.name

