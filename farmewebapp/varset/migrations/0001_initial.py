# Generated by Django 3.0.2 on 2020-01-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='var_data',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('device_id', models.IntegerField(default=0)),
                ('latitude', models.DecimalField(decimal_places=5, default=0, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, default=0, max_digits=8)),
            ],
        ),
    ]
