# Generated by Django 4.1.3 on 2022-11-16 09:55

import cloudinary_storage.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_audio_date_created_alter_audio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 16, 9, 55, 53, 776121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.ImageField(null=True, upload_to='videos/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
