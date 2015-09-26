# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('dailyfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='feed',
            name='unread',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
