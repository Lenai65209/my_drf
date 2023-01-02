from django_filters import rest_framework as filters

from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class TodoFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name='created',
                                   lookup_expr='gte')
    to_date = filters.DateFilter(field_name='created',
                                 lookup_expr='lte')

    class Meta:
        model = Todo
        fields = (
            'project',
            'from_date',
            'to_date',
        )
