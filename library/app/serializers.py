from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birthday_year']


class BookModelSerializer(HyperlinkedModelSerializer):
    # authors = AuthorModelSerializer(many=True) # ломает отражение на frontend

    class Meta:
        model = Book
        fields = ['id', 'name', 'authors']


class BiographyModelSerializer(HyperlinkedModelSerializer):
    # author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    # author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Article
        fields = ['id', 'name', 'author']
