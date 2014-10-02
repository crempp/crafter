# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0003_auto_20140928_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='url',
        ),
        migrations.AddField(
            model_name='server',
            name='host',
            field=models.CharField(default='foo.bar.com', max_length=200),
            preserve_default=False,
        ),
    ]
