# Generated by Django 3.1.4 on 2021-01-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('Texto', models.CharField(blank=True, max_length=500, null=True)),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='coches/')),
                ('Fcreacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('Fmodificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
    ]
