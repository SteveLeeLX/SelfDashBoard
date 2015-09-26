# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyfeed', '0002_auto_20150610_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
