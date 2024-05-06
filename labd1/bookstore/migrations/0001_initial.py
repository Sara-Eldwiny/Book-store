# Generated by Django 5.0.3 on 2024-03-19 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True, unique=True)),
                ('image', models.CharField(max_length=100, null=True)),
                ('pages', models.IntegerField(default=1000, null=True)),
                ('price', models.IntegerField(default=700, null=True, validators=[django.core.validators.MinValueValidator(700), django.core.validators.MaxValueValidator(1000)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]