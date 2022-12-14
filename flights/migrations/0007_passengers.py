# Generated by Django 4.1.1 on 2022-09-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_alter_airport_city_alter_airport_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]
