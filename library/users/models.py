# Create your models here.

from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):  # AbstractBaseUser
    username_validator = ASCIIUsernameValidator()
    id = models.UUIDField(default=uuid4, primary_key=True,
                          help_text=_(
                              "Filled in automatically. Not editable. To edit a user, enter the id in url: 127.0.0.1:8000/api/users/id."))
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. ASCII letters and digits only."),
        validators=[username_validator],
        error_messages=dict(
            unique=_("A user with that username already exists.")),
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Email address."),
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', "email", 'password']

    date_of_birth = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=100, default=1,
                                help_text=_("When saving , it is hashed."))
    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.username)

    def delete(self, *args):
        self.is_active = False
        self.save()
