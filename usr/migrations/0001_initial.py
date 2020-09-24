# Generated by Django 3.1 on 2020-09-23 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('fotografia', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('id_estatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usr.estatus')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usr.roles')),
            ],
        ),
    ]