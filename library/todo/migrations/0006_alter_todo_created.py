# Generated by Django 4.1.4 on 2022-12-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_rename_modified_todo_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]