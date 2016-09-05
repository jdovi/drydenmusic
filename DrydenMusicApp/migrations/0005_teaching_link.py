# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrydenMusicApp', '0004_auto_20160824_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='teaching_link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200, blank=True, null=True)),
                ('scripture', models.CharField(max_length=200, blank=True, null=True)),
                ('author_or_teacher', models.CharField(max_length=200, blank=True, null=True)),
                ('date_presented', models.DateField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
