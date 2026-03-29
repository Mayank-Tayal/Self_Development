from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    # Do not need to give ID as django automatically create ID with auto-incrementing value
    