from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    no_occupants=models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, related_name='user_nieghborhood',null=True)
    email=models.CharField(max_length=50)
    user_id = models.PositiveIntegerField(primary_key=True)

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighborhood= models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)

class Parastatal(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, related_name='neighbor_parastatal',null=True)
    phone_number = models.IntegerField()
