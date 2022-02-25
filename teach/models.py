from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class ToDo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField()

    class Meta:
        verbose_name = ('ToDo')
        verbose_name_plural  = ("Todo")
    
    def __str__(self):
        return self.name