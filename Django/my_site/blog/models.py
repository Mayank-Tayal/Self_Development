from django.db import models
from datetime import date
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f'#{self.caption}'

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail_address = models.EmailField()

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="post")
    tags = models.ManyToManyField(Tag)
    content = models.TextField(null=True)
    date = models.DateField(default=date.today)
    def __str__(self):
        return f"{self.title}"

