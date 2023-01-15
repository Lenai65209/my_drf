# Create your tests here.
import json

from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient, APISimpleTestCase, APITestCase, \
    force_authenticate
from rest_framework.test import APIRequestFactory

from app.models import Author
from app.views import AuthorModelViewSet, BiographyModelViewSet
from todo.views import ProjectModelViewSet
from users.models import CustomUser
from users.views import UserCustomViewSet


class TestAPIRequestFactory(TestCase):

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser('mail@mail.ru', 'Lena')

    def test_get_authors_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_biography_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/biographies/')
        view = BiographyModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_projects_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_authors_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'first_name': 'Александр',
                                                 'last_name': 'Пушкин',
                                                 'birthday_year': 1799},
                               format='json')
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_authors_admin(self):
        factory = APIRequestFactory()

        request = factory.post('/api/authors/', {'first_name': 'Александр',
                                                 'last_name': 'Пушкин',
                                                 'birthday_year': 1799},
                               format='json')
        force_authenticate(request, self.admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_users_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/',
                               {'username': 'Sveta', 'first_name': 'Света',
                                'last_name': 'Светикова',
                                'email': 'mail1@mail.ru',
                                'password': 'password'},
                               format='json')
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_users_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/',
                               {'username': 'Sveta', 'first_name': 'Света',
                                'last_name': 'Светикова',
                                'email': 'mail1@mail.ru',
                                'password': 'password'},
                               format='json')
        force_authenticate(request, self.admin)
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestAPIClient(TestCase):

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser('mail@mail.ru', 'Lena')
        self.author = Author.objects.create(first_name='Александр',
                                            last_name='Пушкин',
                                            birthday_year=1799)
        self.user = CustomUser.objects.create(username='mail@mail.ru',
                                              password='Lena')

    def test_get_author_detail(self):
        client = APIClient()
        response = client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_author_guest(self):
        client = APIClient()
        response = client.put(f'/api/authors/{self.author.id}/',
                              {'first_name': 'Александр', 'last_name': 'Грин',
                               'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_author_admin(self):
        client = APIClient()
        client.force_authenticate(self.admin)
        response = client.put(f'/api/authors/{self.author.id}/',
                              {'first_name': 'Александр', 'last_name': 'Грин',
                               'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.first_name, 'Александр')
        self.assertEqual(author.last_name, 'Грин')
        self.assertEqual(author.birthday_year, 1880)
        client.logout()

    def test_get_user_detail(self):
        client = APIClient()
        response = client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser('mail@mail.ru', 'Lena')
        self.author = Author.objects.create(first_name='Александр',
                                            last_name='Пушкин',
                                            birthday_year=1799)
        self.user = CustomUser.objects.create(username='mail123@mail.ru',
                                              password='Lena123')

    def test_get_books_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_biography_list(self):
        response = self.client.get('/api/biographies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todo_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todo_list_admin(self):
        self.client.login(username='mail@mail.ru', password='Lena')
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_author_mixer(self):
        author = mixer.blend(Author)
        self.client.force_authenticate(self.admin)
        response = self.client.put(f'/api/authors/{author.id}/',
                                   {'first_name': 'Александр',
                                    'last_name': 'Грин',
                                    'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.first_name, 'Александр')
        self.assertEqual(author.last_name, 'Грин')
        self.assertEqual(author.birthday_year, 1880)
        self.client.logout()

    def test_get_author_detail(self):
        author = mixer.blend(Author, first_name='Cергей')
        response = self.client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_author = json.loads(response.content)
        self.assertEqual(response_author['first_name'], 'Cергей')

    def test_get_user_detail(self):
        user = mixer.blend(CustomUser, first_name='Cергей')
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_user = json.loads(response.content)
        self.assertEqual(response_user['first_name'], 'Cергей')

    def test_create_user_admin_guest(self):
        self.client.force_authenticate(self.admin)
        response = self.client.post('/api/users/',
                                    {'username': 'Sveta',
                                     'email': 'mail123@mail.ru',
                                     'password': 'Lena123'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
        response = self.client.post('/api/users/',
                                    {'username': 'Sveta123',
                                     'email': 'mail456@mail.ru',
                                     'password': 'Lena123'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
