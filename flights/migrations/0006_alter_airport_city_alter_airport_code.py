# Generated by Django 4.1.1 on 2022-09-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_remove_flight_t_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(max_length=64, primary_key=''),
        ),
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3, primary_key=''),
        ),
    ]
