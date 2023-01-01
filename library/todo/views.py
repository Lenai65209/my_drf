# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Todo, Project
from .serializers import ProjectModelSerializer, TodoModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
