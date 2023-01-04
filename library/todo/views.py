# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, TodoFilter
from .models import Todo, Project
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # Добавили фильтрацию
    filterset_class = ProjectFilter
    # Добавили пагинацию
    # pagination_class = ProjectLimitOffsetPagination


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    # Добавили фильтрацию по проекту
    # filterset_fields = ['project'] # перенесено в filters.py
    # Добавили пагинацию
    # pagination_class = TodoLimitOffsetPagination
    # Фильтрация по датам
    filterset_class = TodoFilter
