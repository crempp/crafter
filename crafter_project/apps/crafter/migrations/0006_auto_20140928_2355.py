# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0005_auto_20140928_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameconfiguration',
            name='motd',
            field=models.CharField(default=b'', max_length=59, blank=True),
        ),
    ]
