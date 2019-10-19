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
    description = models.CharField(max_length=1000, null=True)
    dateCertified = models.DateField('datetime Certified')
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=3,decimal_places=0)
    requiredScore = models.DecimalField(max_digits=3,decimal_places=0)

class Fertilizer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name Of the product')
    brand = models.CharField(max_length=40, help_text='Name Of the Fertilizer Company')

class Soil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name of Soil Type')
    pH = models.DecimalField(max_digits=5, decimal_places=3)
    nitrogen = models.DecimalField(max_digits=3,decimal_places=0)
    phosphorus = models.DecimalField(max_digits=3,decimal_places=0)
    potassium = models.DecimalField(max_digits=3,decimal_places=0)
    calcium = models.DecimalField(max_digits=3,decimal_places=0)
    copper = models.DecimalField(max_digits=3,decimal_places=0)
    sulphur = models.DecimalField(max_digits=3,decimal_places=0)

class PlantRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, help_text='Name Of the plant')

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    creation = models.DateField(auto_now=False, auto_now_add=False)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE,null=True)
    plantRecipe = models.ForeignKey(PlantRecipe, on_delete=models.CASCADE)
