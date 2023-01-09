from django.contrib.auth.hashers import make_password
from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import CustomUser


class UserSerializer(HyperlinkedModelSerializer):

    # Переопределено, чтобы хешировать password.
    def set_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = CustomUser
        # id добавлено для удобства перехода на редактирование, password - для проверки хеширования.
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'password']
        # fields = "__all__"
