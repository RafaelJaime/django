# Generated by Django 3.1.4 on 2021-02-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reparations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparation',
            old_name='IdCoche',
            new_name='Coche',
        ),
        migrations.RenameField(
            model_name='reparation',
            old_name='IdDueno',
            new_name='Dueno',
        ),
        migrations.RenameField(
            model_name='reparation',
            old_name='IdMecanico',
            new_name='Mecanico',
        ),
    ]
