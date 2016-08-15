# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import storages.backends.s3boto


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('music_file', models.FileField(upload_to='file.pdf', storage=storages.backends.s3boto.S3BotoStorage(acl='private', location='music_files'), null=True, blank=True)),
            ],
        ),
    ]
