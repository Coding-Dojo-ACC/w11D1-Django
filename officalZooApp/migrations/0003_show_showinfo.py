# Generated by Django 2.2 on 2021-05-18 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officalZooApp', '0002_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='showInfo',
            field=models.CharField(default='Show Info', max_length=255),
            preserve_default=False,
        ),
    ]
