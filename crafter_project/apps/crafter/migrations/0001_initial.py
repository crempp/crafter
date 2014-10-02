# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('online', models.BooleanField(default=False)),
                ('online_players', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_flight', models.BooleanField(default=False)),
                ('allow_nether', models.BooleanField(default=True)),
                ('announce_player_achievements', models.BooleanField(default=True)),
                ('difficulty', models.IntegerField(default=1, choices=[(b'Peaceful', 0), (b'Easy', 1), (b'Normal', 2), (b'Hard', 3)])),
                ('enable_command_block', models.BooleanField(default=False)),
                ('enable_query', models.BooleanField(default=False)),
                ('enable_rcon', models.BooleanField(default=False)),
                ('force_gamemode', models.BooleanField(default=False)),
                ('gamemode', models.IntegerField(default=0, choices=[(b'Survival', 0), (b'Creative', 1), (b'Adventure', 2), (b'Spectator', 3)])),
                ('generate_structures', models.BooleanField(default=True)),
                ('generator_settings', models.CharField(default=b'', max_length=300, blank=True)),
                ('hardcore', models.BooleanField(default=False)),
                ('level_name', models.CharField(max_length=200)),
                ('level_seed', models.CharField(default=b'', max_length=128, blank=True)),
                ('level_type', models.CharField(default=b'DEFAULT', max_length=128, choices=[(b'DEFAULT', b'DEFAULT'), (b'FLAT', b'FLAT'), (b'LARGEBIOMES', b'LARGEBIOMES'), (b'AMPLIFIED', b'AMPLIFIED'), (b'CUSTOMIZED', b'CUSTOMIZED')])),
                ('max_build_height', models.IntegerField(default=256)),
                ('max_players', models.IntegerField(default=20)),
                ('max_tick_time', models.IntegerField(default=60000)),
                ('max_world_size', models.IntegerField(default=29999984)),
                ('motd', models.CharField(max_length=59)),
                ('network_compression_threshold', models.IntegerField(default=256)),
                ('online_mode', models.BooleanField(default=True)),
                ('op_permission_level', models.IntegerField(default=4, choices=[(b'can bypass spawn protection', 0), (b'can use /clear, /difficulty, /effect, /gamemode, /gamerule, /give, and /tp, and can edit command blocks', 1), (b'can use /ban, /deop, /kick, and /op', 2), (b'can use /stop', 3)])),
                ('player_idle_timeout', models.IntegerField(default=0)),
                ('pvp', models.BooleanField(default=True)),
                ('query_port', models.IntegerField(default=25565)),
                ('rcon_password', models.CharField(default=b'', max_length=128, blank=True)),
                ('rcon_port', models.IntegerField(default=25575)),
                ('resource_pack_hash', models.CharField(default=b'', max_length=128, blank=True)),
                ('resource_pack', models.CharField(default=b'', max_length=128, blank=True)),
                ('server_ip', models.CharField(default=b'', max_length=15, blank=True)),
                ('server_port', models.IntegerField(default=25565)),
                ('snooper_enabled', models.BooleanField(default=True)),
                ('spawn_animals', models.BooleanField(default=True)),
                ('spawn_monsters', models.BooleanField(default=True)),
                ('spawn_npcs', models.BooleanField(default=True)),
                ('spawn_protection', models.IntegerField(default=16)),
                ('texture_pack', models.CharField(default=b'', max_length=128, blank=True)),
                ('view_distance', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(3)])),
                ('white_list', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=250)),
                ('version', models.CharField(max_length=10)),
                ('jar_name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('uuid', models.CharField(max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='configuration',
            field=models.OneToOneField(related_name=b'configuration_of', to='crafter.GameConfiguration'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='server',
            field=models.ForeignKey(to='crafter.Server'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='version',
            field=models.ForeignKey(to='crafter.GameVersion'),
            preserve_default=True,
        ),
    ]
