# Generated by Django 3.1.4 on 2021-01-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210124_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]