# Generated by Django 3.1 on 2020-08-24 10:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20200824_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='Идентификатор'),
        ),
    ]