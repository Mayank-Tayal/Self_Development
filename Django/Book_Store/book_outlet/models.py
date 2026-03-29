from django.db import models
from django.core.validators import MinLengthValidator,MaxValueValidator
from django.urls import reverse
# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxValueValidator(5)]
        )
    author = models.CharField(null=True, max_length=100)
    isBestSelling = models.BooleanField(default=False)
    # Do not need to give ID as django automatically create ID with auto-incrementing value
     
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    

    def __str__(self):
       return f"{self.title} ({self.rating})"