# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161120_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='intime',
        ),
    ]
