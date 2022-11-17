# Generated by Django 4.1.3 on 2022-11-16 12:41

import cloudinary_storage.storage
import cloudinary_storage.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_audio_date_created_alter_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 16, 12, 41, 27, 221095, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='kin-keepers/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
