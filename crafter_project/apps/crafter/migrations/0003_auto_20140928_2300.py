# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0002_auto_20140928_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='configuration',
        ),
        migrations.AddField(
            model_name='gameconfiguration',
            name='game',
            field=models.ForeignKey(default=1, to='crafter.Game'),
            preserve_default=False,
        ),
    ]
