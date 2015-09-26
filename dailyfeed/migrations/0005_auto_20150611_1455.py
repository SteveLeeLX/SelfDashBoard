# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyfeed', '0004_auto_20150611_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
