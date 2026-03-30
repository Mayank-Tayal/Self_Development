from django.db import models
from django.core.validators import MinLengthValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.



class Book(models.Model):
    # Do not need to give ID as django automatically create ID with auto-incrementing value
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxValueValidator(5)]
        )
    author = models.CharField(null=True, max_length=100)
    isBestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,blank=True, db_index=True)
    # editable=False removes the field, in admin readonly allows to show but not able to edit
    # editable=False needs to be removed for use of prepopulated in admin
    # blank=True allows field to be empty

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])


    # does not need this method as prepopulated_fields in admin already calls slugify
    # while entering new entries to database 
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.title} ({self.rating})"