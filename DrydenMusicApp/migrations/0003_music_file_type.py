# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrydenMusicApp', '0002_auto_20160815_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='file_type',
            field=models.IntegerField(choices=[(1, 'Single Song Sheet'), (2, 'Songbook')], default=1),
        ),
    ]
