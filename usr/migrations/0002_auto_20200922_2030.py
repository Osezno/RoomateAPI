# Generated by Django 3.1 on 2020-09-23 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='estatus',
            table='estatus',
        ),
        migrations.AlterModelTable(
            name='roles',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuarios',
        ),
    ]
