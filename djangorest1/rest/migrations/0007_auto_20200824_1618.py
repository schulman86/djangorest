# Generated by Django 3.1 on 2020-08-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_auto_20200824_1601'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='reference',
            constraint=models.UniqueConstraint(fields=('uuid', 'version'), name='id_ver'),
        ),
    ]