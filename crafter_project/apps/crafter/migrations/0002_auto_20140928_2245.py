# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='configuration',
            field=models.OneToOneField(to='crafter.GameConfiguration'),
        ),
    ]
