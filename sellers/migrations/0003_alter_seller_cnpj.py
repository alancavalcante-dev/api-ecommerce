# Generated by Django 5.1.1 on 2024-09-16 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_rename_sellers_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='cnpj',
            field=models.CharField(max_length=14, validators=[django.core.validators.MinLengthValidator(14)]),
        ),
    ]
