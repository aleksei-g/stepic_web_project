# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20160310_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
