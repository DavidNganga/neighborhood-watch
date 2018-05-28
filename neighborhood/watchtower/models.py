from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    no_occupants=models.IntegerField(null=True)
    event_details = models.TextField(max_length=50)

    @classmethod
    def get_all(cls):
        hoods = cls.objects.all()
        return hoods

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def get_Neighborhood_by_id(cls,id):
        names = cls.objects.get(id=id)
        return names

    @classmethod
    def search(cls,search_term):
         names = cls.objects.filter(name__icontains=search_term)
         return names

class Profile(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, related_name='user_nieghborhood',null=True)
    email=models.CharField(max_length=50)


    @classmethod
    def get_all(cls):
        bros = cls.objects.all()
        return bros

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def get_User_by_id(cls,id):
        usser = cls.objects.get(id=id)
        return usser

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighborhood= models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)
    description =models.TextField(max_length=250)

    @classmethod
    def get_all(cls):
        businesses = cls.objects.all()
        return businesses

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def get_Business_by_id(cls,id):
        bags = cls.objects.get(id=id)
        return bags

    @classmethod
    def search(cls,search_term):
         names = cls.objects.filter(name__icontains=search_term)
         return names


class Parastatal(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, related_name='neighbor_parastatal',null=True)
    phone_number = models.IntegerField()
