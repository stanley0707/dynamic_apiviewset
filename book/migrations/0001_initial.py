# Generated by Django 2.1.7 on 2020-07-10 12:56

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, unique=True, validators=[book.models.validate_not_empty])),
                ('born_date', models.DateTimeField(blank=True, null=True)),
                ('rip_date', models.DateTimeField(blank=True, null=True)),
                ('secret', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True, validators=[book.models.validate_not_empty])),
                ('description', models.TextField()),
                ('secret', models.CharField(blank=True, max_length=50)),
                ('authors', models.ManyToManyField(related_name='author_books', to='book.Author')),
            ],
        ),
    ]
