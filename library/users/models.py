# Create your models here.

from django.db import models
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    id = models.URLField(default=uuid4, primary_key=True)
    username = models.CharField(
        _("username"),
        # default=id,
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. ASCII letters and digits only."),
        validators=[username_validator],
        error_messages=dict(
            unique=_("A user with that username already exists.")),
    )
    email = models.CharField(
        _("email address"),
        max_length=256,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    def delete(self, *args):
        self.deleted = True
        self.save()
