# Generated by Django 2.2 on 2021-05-05 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalName', models.CharField(max_length=45)),
                ('animalType', models.CharField(max_length=45)),
                ('animalBirth', models.DateTimeField()),
                ('animalAdded', models.DateTimeField(auto_now_add=True)),
                ('animalUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]