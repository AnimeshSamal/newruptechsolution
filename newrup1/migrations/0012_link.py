# Generated by Django 4.0.2 on 2023-08-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0011_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('doc', models.FileField(upload_to='doc')),
            ],
        ),
    ]