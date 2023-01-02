# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .filters import ArticleFilter, BookFilter
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer
from .serializers import BiographyModelSerializer, ArticleModelSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = BookModelSerializer


class BiographyModelViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    filterset_fields = ['name', 'user']
    filterset_class = ArticleFilter
    pagination_class = ArticleLimitOffsetPagination


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1


class BookDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filterset_fields = ['name', 'user', 'authors']
    filterset_class = BookFilter
    pagination_class = BookLimitOffsetPagination
