# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('sender', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=20000)),
                ('important', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
