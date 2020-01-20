# Generated by Django 3.0.2 on 2020-01-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('device_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=5, default=0, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=5, default=0, max_digits=7)),
                ('amb_ll', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('temp', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('loc_humidity', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm1', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm2', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm3', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm4', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm5', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm6', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm7', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('sm8', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
            ],
        ),
    ]
