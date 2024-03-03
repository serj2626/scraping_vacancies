# Generated by Django 5.0.1 on 2024-01-08 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='название города')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='язык программирования')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='ссылка')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('company', models.CharField(max_length=250, verbose_name='компания')),
                ('description', models.TextField(verbose_name='описание вакансии')),
                ('timestamp', models.DateField(auto_now_add=True, verbose_name='дата добавления вакансии')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language', verbose_name='язык программирования')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancys',
            },
        ),
    ]
