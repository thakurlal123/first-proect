from django.db import models

# Create your models here.
class Home(models.model):
    Name = models.CharField(max_length=122)
    Mail = models.CharField(max_length=122)
    Note = models.TimeField()
    time = models.DateField()
    