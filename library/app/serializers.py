from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birthday_year']


class BookModelSerializer(HyperlinkedModelSerializer):
    # authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'
