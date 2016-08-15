# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DrydenMusicApp.models
from django.utils.timezone import utc
import storages.backends.s3boto
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('DrydenMusicApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 18, 14, 43, 265487, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='first_line',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(null=True, upload_to=DrydenMusicApp.models.data_file_path, storage=storages.backends.s3boto.S3BotoStorage(acl='private', location='music_files'), blank=True),
        ),
    ]
