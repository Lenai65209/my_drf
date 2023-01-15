# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.permissions import IsAuthenticated, AllowAny

from .filters import ArticleFilter, BookFilter
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, \
    ArticleSerializer
from .serializers import BiographyModelSerializer, ArticleModelSerializer
from .serializers import BookSerializer, BiographySerializer


# class SuperUserOnly(BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.is_superuser


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]  # Для пповерки


# class BookModelViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     serializer_class = BookModelSerializer


class BiographyModelViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]  # Для пповерки

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BiographySerializer
        return BiographyModelSerializer


# class ArticleModelViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer


# class ArticleCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     # permission_classes = [SuperUserOnly]

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'user']
    # filterset_class = ArticleFilter
    # pagination_class = ArticleLimitOffsetPagination
    # permission_classes = [IsAuthenticated]  # Для пповерки

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ArticleSerializer
        return ArticleModelSerializer


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1


class BookDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['name', 'user', 'authors']
    filterset_class = BookFilter
    # pagination_class = BookLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookModelSerializer
