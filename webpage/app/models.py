from django.db import models

# Create your models here.
class Greenhouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone =  models.CharField(max_length=20)
    joinDate = models.DateField(auto_now=False, auto_now_add=False)

class Certification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name Of the Greenhouse')
    dateCertified = models.DateField('datetime Certified')
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=3,decimal_places=0)
    requiredScore = models.DecimalField(max_digits=3,decimal_places=0)

class Fertilizer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name Of the product')
    brand = models.CharField(max_length=40, help_text='Name Of the Fertilizer Company')

class PlantRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name Of the plant')

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    creation = models.DateField(auto_now=False, auto_now_add=False)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    plantRecipe = models.ForeignKey(PlantRecipe, on_delete=models.CASCADE)
