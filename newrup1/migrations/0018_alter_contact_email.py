# Generated by Django 3.2.20 on 2023-08-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0017_auto_20230804_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]