# Create your models here.
from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.URLField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.last_name

    def delete(self, *args):
        self.deleted = True
        self.save()