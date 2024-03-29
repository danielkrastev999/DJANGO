# Generated by Django 5.0.1 on 2024-01-16 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre de la Competicion')),
                ('lugar', models.CharField(max_length=50, verbose_name='Lugar')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación de la competicion')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación de la competicion')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Equipo')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del Equipo')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del Equipo')),
                ('competicion', models.ManyToManyField(to='principal.competicion', verbose_name='Competicion')),
                ('responable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Comentario del articulo')),
                ('correo', models.EmailField(max_length=254)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='Foto')),
                ('edad', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del comentario')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del comentario')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.equipo')),
            ],
        ),
    ]
