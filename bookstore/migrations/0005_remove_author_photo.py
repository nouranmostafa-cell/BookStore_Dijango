# Generated by Django 5.2 on 2025-04-26 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_author_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
    ]
