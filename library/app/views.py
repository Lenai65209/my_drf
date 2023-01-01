# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer
from .serializers import BiographyModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer
