# Generated by Django 4.1.4 on 2023-01-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(null=True)),
                ('hum', models.FloatField(null=True)),
                ('dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
