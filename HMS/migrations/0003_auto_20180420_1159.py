# Generated by Django 2.0.3 on 2018-04-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0002_auto_20180420_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Customer'), (2, 'Admin')]),
        ),
    ]
