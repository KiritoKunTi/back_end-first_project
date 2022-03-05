# Generated by Django 4.0.2 on 2022-03-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Мейрам атауы')),
                ('on_date', models.CharField(max_length=20, verbose_name='Күн-айы')),
                ('anons', models.TextField(verbose_name='Мейрам жайлы')),
            ],
        ),
    ]
