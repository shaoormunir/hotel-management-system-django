# Generated by Django 2.0.4 on 2018-04-21 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0006_auto_20180421_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.IntegerField(choices=[(1, 'Standard'), (2, 'Family'), (3, 'Business'), (4, 'Presidential')])),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('electronic_safe', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('room_service', models.BooleanField(default=False)),
                ('hair_dryer', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('bar', models.BooleanField(default=False)),
                ('pick_up', models.BooleanField(default=False)),
                ('spa', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('restaurant', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Room Type',
                'verbose_name_plural': 'Room Types',
            },
        ),
        migrations.RemoveField(
            model_name='room',
            name='bar',
        ),
        migrations.RemoveField(
            model_name='room',
            name='electronic_safe',
        ),
        migrations.RemoveField(
            model_name='room',
            name='gym',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pick_up',
        ),
        migrations.RemoveField(
            model_name='room',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_service',
        ),
        migrations.RemoveField(
            model_name='room',
            name='spa',
        ),
        migrations.RemoveField(
            model_name='room',
            name='swimming_pool',
        ),
        migrations.RemoveField(
            model_name='room',
            name='wifi',
        ),
        migrations.AlterField(
            model_name='image',
            name='room_type',
            field=models.ForeignKey(help_text='Enter the room type for which you want to add an image', on_delete=django.db.models.deletion.CASCADE, to='HMS.RoomType'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMS.RoomType'),
        ),
    ]
