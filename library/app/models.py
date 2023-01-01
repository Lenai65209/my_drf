# Create your models here.
from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.URLField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.last_name}  {self.first_name}'

    def delete(self, *args):
        self.deleted = True
        self.save()


class Biography(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)


# class Article(models.Model):
#     name = models.CharField(max_length=32)
#     author = models.ForeignKey(Author, models.PROTECT)