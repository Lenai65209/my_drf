# Generated by Django 4.1.4 on 2022-12-30 18:09

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_project_todo_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated',
        ),
        migrations.AddField(
            model_name='todo',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.URLField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]