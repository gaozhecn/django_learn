# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.IntegerField(default=datetime.datetime(2016, 11, 20, 13, 27, 20, 671832, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
