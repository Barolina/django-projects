# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='country',
            field=models.CharField(default='China', max_length=50),
            preserve_default=False,
        ),
    ]
