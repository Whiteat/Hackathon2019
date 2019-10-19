from django.db import models

class Certification(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    ##my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    id = models.AutoField(primary_key=true)
    name = models.CharField(max_length=40, help_text='Name Of the Greenhouse')
    type = models.CharField(max_length=40, help_text='Type of plant annual/paranual')
    date_added = models.DateTimeField('date added')


    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
