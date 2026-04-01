from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField( max_length=2)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Country List"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'
    
    # Can add nested class for meta congiguration fopr django
    # means to add special setting how data to store in DB or how data renders in 
    # forms
    class Meta:
        verbose_name_plural = "Address Enteries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    # Do not need to give ID as django automatically create ID with auto-incrementing value
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  null=True, related_name="books")
    isBestSelling = models.BooleanField(default=False)
    published_country = models.ManyToManyField(Country, )
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