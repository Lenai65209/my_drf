from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birthday_year']


class BookModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

class ArticleModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
