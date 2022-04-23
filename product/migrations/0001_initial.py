# Generated by Django 4.0.4 on 2022-04-22 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model_no', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')])),
                ('product_comp_name', models.CharField(max_length=200)),
                ('pic1', models.ImageField(default='default.jpg', upload_to='product')),
            ],
        ),
    ]