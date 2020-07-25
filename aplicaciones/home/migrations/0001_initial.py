# Generated by Django 3.0.8 on 2020-07-22 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('Nacionalidad', models.CharField(max_length=100, verbose_name='Nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('Resumen', models.TextField(blank=True, verbose_name='Resumen')),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('Resumen', models.TextField(blank=True, verbose_name='Resumen')),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Autor')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Categoria')),
            ],
        ),
    ]