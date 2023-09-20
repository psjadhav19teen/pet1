from django.db import models
from django.utils.html import mark_safe
# Create your models here.
class Pet(models.Model):
    gender=(("male","male"),("female","female"))
    image=models.ImageField(upload_to="img%y")
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30,choices=gender)
    species=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    age=models.IntegerField()
    description=models.CharField(max_length=500)

  

    