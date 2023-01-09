# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import CustomUser
from .serializers import UserSerializer


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
