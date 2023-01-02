from django.db import models
from django.utils import timezone

from users.models import CustomUser


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    repo = models.URLField(max_length=200)
    # path="https://github.com/Lenai65209/my_drf"
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        """A string representation of the model."""
        return f'{self.title} - {self.repo}'


class Todo(models.Model):
    project = models.ManyToManyField(Project)
    text = models.TextField(max_length=1000)
    # Не отражаются в панели администратора.
    # created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    # updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)
    users = models.ForeignKey(CustomUser, models.PROTECT)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.created:
            self.created = timezone.now()
        else:
            self.updated = timezone.now()
        return super(Todo, self).save(*args, **kwargs)

    def delete(self, *args):  # из формы заметки
        self.active = False  # пповерка работы поля active.
        self.save()
