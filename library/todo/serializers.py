from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'repo', 'users']


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['project', 'text', 'users', 'active']
