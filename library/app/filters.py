from django_filters import rest_framework as filters

from .models import Article, Book


class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['name', 'author']


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Book
        fields = ['name', 'authors']
