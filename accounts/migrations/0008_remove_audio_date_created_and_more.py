# Generated by Django 4.1.3 on 2022-11-15 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_audio_alter_customer_date_created_delete_audios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 9, 0, 20, 753572, tzinfo=datetime.timezone.utc)),
        ),
    ]
