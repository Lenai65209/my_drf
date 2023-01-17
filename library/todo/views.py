# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, TodoFilter
from .models import Todo, Project
from .serializers import ProjectModelSerializer, TodoModelSerializer, \
    ProjectModelSerializerV2, TodoModelSerializerV2


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    # serializer_class = ProjectModelSerializer  # для версий API
    # Добавили фильтрацию
    filterset_class = ProjectFilter

    # Добавили пагинацию
    # pagination_class = ProjectLimitOffsetPagination

    #  Проверка: 127.0.0.1:8000/api/projects/?version=2.0
    def get_serializer_class(self):
        if self.request.version == '2.0' and self.request.method in ['GET']:
            return ProjectModelSerializerV2
        return ProjectModelSerializer


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    # serializer_class = TodoModelSerializer  # для версий API
    # Добавили фильтрацию по проекту
    # filterset_fields = ['project'] # перенесено в filters.py
    # Добавили пагинацию
    # pagination_class = TodoLimitOffsetPagination
    # Фильтрация по датам
    filterset_class = TodoFilter

    # permission_classes = [IsAuthenticated] # для проверки

    #  Проверка: 127.0.0.1:8000/api/todos/?version=2.0
    def get_serializer_class(self):
        if self.request.version == '2.0' and self.request.method in ['GET']:
            return TodoModelSerializerV2
        return TodoModelSerializer
