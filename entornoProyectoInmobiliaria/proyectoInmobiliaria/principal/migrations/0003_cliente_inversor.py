# Generated by Django 5.0 on 2023-12-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_cliente_alter_piso_fechaalta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='inversor',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
