# Register your models here.
from django.contrib import admin

from .models import Author, Biography, Book, Article


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
