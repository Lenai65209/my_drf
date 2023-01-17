from rest_framework.serializers import HyperlinkedModelSerializer, \
    ModelSerializer

from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birthday_year']


class AuthorModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birthday_year']


class BookModelSerializer(HyperlinkedModelSerializer):
    # authors = AuthorModelSerializer(many=True) # ломает отражение на frontend

    class Meta:
        model = Book
        fields = ['id', 'name', 'authors']


class BookModelSerializerV2(ModelSerializer):
    authors = AuthorModelSerializer(many=True) # ломает отражение на frontend

    class Meta:
        model = Book
        fields = ['name', 'authors']


class BookSerializer(ModelSerializer):
    authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    # author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Biography
        fields = ['id', 'text', 'author']
        # fields = '__all__'


class BiographyModelSerializerV2(HyperlinkedModelSerializer):
    author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Biography
        fields = ['text', 'author']
        # fields = '__all__'


class BiographySerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    # author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Article
        fields = ['id', 'name', 'author']


class ArticleModelSerializerV2(HyperlinkedModelSerializer):
    author = AuthorModelSerializer() # ломает отражение на frontend

    class Meta:
        model = Article
        fields = ['name', 'author']


class ArticleSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'
