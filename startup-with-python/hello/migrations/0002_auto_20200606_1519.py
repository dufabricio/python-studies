# Generated by Django 2.2.13 on 2020-06-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='TodoItem',
        ),
    ]
