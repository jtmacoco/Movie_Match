# Generated by Django 3.2.9 on 2021-11-13 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_moviemodel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviemodel',
            name='author',
        ),
    ]
