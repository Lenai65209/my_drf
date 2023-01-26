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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.views.generic import TemplateView

from app.views import AuthorModelViewSet\
    # , BookModelViewSet, ArticleModelViewSet, ArticleCustomViewSet,
from app.views import BiographyModelViewSet,  \
     BookDjangoFilterViewSet, ArticleDjangoFilterViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
# from users.views import UserModelViewSet
from users.views import UserCustomViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register("authors", AuthorModelViewSet)
# router.register("books", BookModelViewSet)
router.register("books", BookDjangoFilterViewSet)
router.register("biographies", BiographyModelViewSet)
# router.register("article_model", ArticleModelViewSet)
# router.register("article_custom", ArticleCustomViewSet)
router.register("articles", ArticleDjangoFilterViewSet)
# router.register("users", UserModelViewSet)
router.register("users", UserCustomViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Проверка: 127.0.0.1:8000/swagger.json/
    # path('swagger<str:format>/', schema_view.without_ui()),

    # Проверка: 127.0.0.1:8000/swagger.json/
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    #  М.б. декоратором, или вызван явно, и передать в него View (csrf токен не проверяется).
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))), #  может быть декоратором.
#  Для проверки работы build
    path('', TemplateView.as_view(template_name='index.html'))
]
