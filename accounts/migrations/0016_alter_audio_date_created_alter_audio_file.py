# Generated by Django 4.1.3 on 2022-11-16 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_audio_date_created_alter_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 16, 9, 6, 33, 12767, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
