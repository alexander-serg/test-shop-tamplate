# Generated by Django 4.0 on 2022-01-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemimage',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Главная'),
        ),
    ]
