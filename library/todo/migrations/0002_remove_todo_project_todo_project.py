# Generated by Django 4.1.4 on 2022-12-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='project',
        ),
        migrations.AddField(
            model_name='todo',
            name='project',
            field=models.ManyToManyField(to='todo.project'),
        ),
    ]
