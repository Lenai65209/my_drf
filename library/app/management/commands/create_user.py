from django.contrib.auth.models import User
from django.core.management import BaseCommand

from app.models import Book, Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User:
            User.objects.create_superuser(username="Lena", password="123456",
                                          email="admin.admin.ru")
            data_author = {'first_name': 'Александр',
                           'last_name': 'Пушкин',
                           'birthday_year': 1799
                           }

            author = Author.objects.create(**data_author)
            book = Book.objects.create(name="Руслан и Людмила")
            book.authors.add(author.id)
