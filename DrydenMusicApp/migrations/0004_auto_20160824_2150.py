# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DrydenMusicApp.models
import storages.backends.s3boto


class Migration(migrations.Migration):

    dependencies = [
        ('DrydenMusicApp', '0003_music_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='author_or_teacher',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='music',
            name='date_presented',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='music',
            name='scripture',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='music',
            name='topic',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='file_type',
            field=models.IntegerField(default=1, choices=[(1, 'Single Song Sheet'), (2, 'Songbook'), (3, 'Teaching')]),
        ),
        migrations.AlterField(
            model_name='music',
            name='first_line',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(null=True, upload_to=DrydenMusicApp.models.data_file_path, storage=storages.backends.s3boto.S3BotoStorage(location='music_files')),
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
