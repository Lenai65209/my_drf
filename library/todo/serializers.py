from rest_framework.serializers import HyperlinkedModelSerializer, \
    ModelSerializer

from .models import Project, Todo


#  HyperlinkedModelSerializer не работает для front
class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        # id добавлено для удобства перехода на редактирование,
        fields = ['id', 'title', 'repo', 'users']


class ProjectModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        # id добавлено для удобства перехода на редактирование,
        fields = ['title', 'repo', 'users']


#  HyperlinkedModelSerializer не работает для front
class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        # id добавлено для удобства перехода на редактирование,
        fields = ['id', 'project', 'text', 'users', 'active']


class TodoModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        # id добавлено для удобства перехода на редактирование,
        fields = ['project', 'text', 'users', 'active']
