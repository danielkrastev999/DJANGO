# Generated by Django 5.0.1 on 2024-02-08 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_competicion_responsable_alter_equipo_competicion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competicion',
            name='responsable',
        ),
    ]
