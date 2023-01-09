from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):

    # Для создания хешированного пароля из админки.
    def save_model(self, request, obj, change, *args, **kwargs):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()
