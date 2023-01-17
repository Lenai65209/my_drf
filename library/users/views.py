# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import CustomUser
from .serializers import UserSerializer, UserSerializerV2


# class UserModelViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


# mixins.CreateModelMixin # Добавлено для проверки возможности создания в API.
class UserCustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    #  Проверка: 127.0.0.1:8000/api/users/?version=2.0
    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserSerializerV2
        return UserSerializer
