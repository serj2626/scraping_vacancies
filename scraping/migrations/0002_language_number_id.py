# Generated by Django 5.0.1 on 2024-03-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='number_id',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='номер в списке'),
        ),
    ]
