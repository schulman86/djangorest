# Generated by Django 3.1 on 2020-08-24 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20200824_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='parent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.reference'),
        ),
    ]
