# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 4, 59, 15, 416644, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 4, 59, 22, 41788, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
