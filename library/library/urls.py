"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

from app.views import AuthorModelViewSet, BookModelViewSet
from app.views import BiographyModelViewSet, ArticleModelViewSet, \
    ArticleCustomViewSet, BookDjangoFilterViewSet, ArticleDjangoFilterViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
# from users.views import UserModelViewSet
from users.views import UserCustomViewSet

router = DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register("books", BookModelViewSet)
router.register("books_filter_pagination", BookDjangoFilterViewSet)
router.register("biographies", BiographyModelViewSet)
router.register("article_model", ArticleModelViewSet)
router.register("article_custom", ArticleCustomViewSet)
router.register("article_filter_pagination", ArticleDjangoFilterViewSet)
# router.register("users", UserModelViewSet)
router.register("users", UserCustomViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),
]
