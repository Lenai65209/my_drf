from django.contrib import admin

from .models import Project, Todo


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
