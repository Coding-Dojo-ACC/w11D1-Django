# Generated by Django 2.2 on 2021-05-13 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officalZooApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employeeZoo',
        ),
        migrations.AddField(
            model_name='employee',
            name='zoo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='officalZooApp.Zoo'),
            preserve_default=False,
        ),
    ]
