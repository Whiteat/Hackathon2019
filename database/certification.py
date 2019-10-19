from django.db import models

class Certification(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    ##my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    id = models.AutoField(primary_key=true)
    name = models.CharField(max_length=40, help_text='Name Of the Greenhouse')
    dateCertified = models.DateField('datetime Certified')
    greenHouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    type = models.CharField()
    score = models.DecimalField(max_digits=3,decimal_places=0)
    requiredScore = models.DecimalField(max_digits=3,decimal_places=0)


    ...


    def __str__(self):
        return self.name
