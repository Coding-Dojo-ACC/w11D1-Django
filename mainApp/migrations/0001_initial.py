# Generated by Django 2.2 on 2021-05-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=45)),
                ('addedSkill', models.DateTimeField(auto_now_add=True)),
                ('updatedSkill', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
