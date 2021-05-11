from django.db import models

# Create your models here.

class Frage(models.Model): 
    id = models.IntegerField(primary_key=True)
    themaId = models.IntegerField()
    userId = models.IntegerField()

