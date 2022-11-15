# Generated by Django 4.0.2 on 2022-11-14 14:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 14, 14, 34, 46, 894409, tzinfo=utc)),
        ),
    ]
