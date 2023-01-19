import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from app.models import Book, Author
from todo.models import Project, Todo
from users.models import CustomUser


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")
#
# schema = graphene.Schema(query=Query)


# ________________________________________________________________________________


# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class Query(graphene.ObjectType):
#     all_books = graphene.List(BookType)
#     all_authors = graphene.List(AuthorType)
#
#     def resolve_all_books(root, info):
#         return Book.objects.all()
#
#     def resolve_all_authors(root, info):
#         return Author.objects.all()
#
#
# schema = graphene.Schema(query=Query)

# _______________________________________________________________________________


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(root, info):
        return Author.objects.all()

    all_users = graphene.List(CustomUserType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_author_by_id(root, info, id):
        try:
            return Author.objects.get(id=id)

        except Author.DoesNotExist:
            return None

    books_by_author = graphene.List(BookType,
                                    last_name=graphene.String(required=False))

    def resolve_books_by_author(root, info, last_name=None):
        books = Book.objects.all()
        if last_name:
            books = books.filter(authors__last_name=last_name)
        return books

    projects_by_user = graphene.List(ProjectType,
                                     username=graphene.String(required=False))

    def resolve_projects_by_user(root, info, username=None):
        projects = Project.objects.all()
        if username:
            projects = projects.filter(users__username=username)
        return projects

    todos_by_user = graphene.List(TodoType,
                                     username=graphene.String(required=False))

    def resolve_todos_by_user(root, info, username=None):
        todos = Todo.objects.all()
        if username:
            todos = todos.filter(users__username=username)
        return todos

    author_by_name = graphene.List(AuthorType,
                                   first_name=graphene.String(required=False),
                                   last_name=graphene.String(required=False))

    def resolve_author_by_name(root, info, first_name=None, last_name=None):
        if not first_name and last_name:
            return Author.objects.all()
        params = {}
        if first_name:
            params['first_name__contains'] = first_name
        if last_name:
            params['last_name__contains'] = last_name
        return Author.objects.filter(**params)


schema = graphene.Schema(query=Query)


# _______________________________________________________________________________


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        author = Author.objects.create(**kwargs)
        return cls(author=author)


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        birthday_year = graphene.Int(required=False)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id=None, first_name=None, last_name=None,
               birthday_year=None):
        author = Author.objects.get(id=id)
        if first_name:
            author.first_name = first_name
        if last_name:
            author.last_name = last_name
        if birthday_year:
            author.birthday_year = birthday_year
        if first_name or last_name or birthday_year:
            author.save()
        return cls(author=author)


# class AuthorDeleteMutation(graphene.Mutation):
#     ok = graphene.Boolean()
#
#     class Arguments:
#         id = graphene.ID(required=True)
#
#     author = graphene.Field(AuthorType)
#     authors = graphene.List(AuthorType)
#
#     @classmethod
#     def mutate(cls, root, info, id=None):
#         author = Author.objects.get(id=id)
#         author.delete()
#         return cls(ok=True)


class Mutations(ObjectType):
    create_author = AuthorCreateMutation.Field()
    update_author = AuthorUpdateMutation.Field()
    # delete_author = AuthorDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

# _____________________________________________________________________
