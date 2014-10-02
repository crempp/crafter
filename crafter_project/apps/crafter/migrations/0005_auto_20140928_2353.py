# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0004_auto_20140928_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameconfiguration',
            name='difficulty',
            field=models.IntegerField(default=1, choices=[(0, b'Peaceful'), (1, b'Easy'), (2, b'Normal'), (3, b'Hard')]),
        ),
        migrations.AlterField(
            model_name='gameconfiguration',
            name='game',
            field=models.OneToOneField(to='crafter.Game'),
        ),
        migrations.AlterField(
            model_name='gameconfiguration',
            name='gamemode',
            field=models.IntegerField(default=0, choices=[(0, b'Survival'), (1, b'Creative'), (2, b'Adventure'), (3, b'Spectator')]),
        ),
        migrations.AlterField(
            model_name='gameconfiguration',
            name='op_permission_level',
            field=models.IntegerField(default=4, choices=[(0, b'can bypass spawn protection'), (1, b'can use /clear, /difficulty, /effect, /gamemode, /gamerule, /give, and /tp, and can edit command blocks'), (2, b'can use /ban, /deop, /kick, and /op'), (3, b'can use /stop')]),
        ),
    ]
