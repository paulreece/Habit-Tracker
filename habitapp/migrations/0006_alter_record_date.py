# Generated by Django 4.0.3 on 2022-03-23 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitapp', '0005_alter_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
