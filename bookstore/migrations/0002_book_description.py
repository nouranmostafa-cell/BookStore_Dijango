# Generated by Django 5.2 on 2025-04-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, help_text='Detailed description of the book', null=True),
        ),
    ]
