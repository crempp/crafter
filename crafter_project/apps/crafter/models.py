from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

ConfigurationMeta = {
    'allow-flight': 'Allows users to use flight on your server while in '
        'Survival mode, if they have a mod that provides flight installed.',

    'allow-nether': 'Allows players to travel to the Nether.',

    'announce-player-achievements': 'Allows server to announce when a player '
        'gets an achievement.',

    'difficulty': 'Defines the difficulty (such as damage dealt by mobs and '
        'the way hunger and poison affects players) of the server.',

    'enable-command-block': 'Enables command blocks',

    'enable-query': 'Enables GameSpy4 protocol server listener. Used to get '
        'information about server.',

    'enable-rcon': 'Enables remote access to the server console.',

    'force-gamemode': 'Force players to join in the default game mode.',

    'gamemode': 'Defines the mode of gameplay.',

    'generate-structures': 'Defines whether structures (such as villages) will '
        'be generated.',

    'generator-settings': 'The settings used to customize world generation. '
        'See Superflat and Customized for possible settings and examples.',

    'hardcore': 'If set to true, players will be permanently banned if they '
        'die.',

    'level-name': 'The "level-name" value will be used as the world name and '
        'its folder name. You may also copy your saved game folder here, and '
        'change the name to the same as that folder\'s to load it instead.',

    'level-seed': 'Add a seed for your world, as in Singleplayer.',

    'level-type': 'Determines the type of map that is generated.',

    'max-build-height': 'The maximum height in which building is allowed. '
        'Terrain may still naturally generate above a low height limit.',

    'max-players': 'The maximum number of players that can play on the server '
        'at the same time. Note that if more players are on the server it will '
        'use more resources. Note also, op player connections are not supposed '
        'to count against the max players, but ops currently cannot join a '
        'full server. Extremely large values for this field result in the '
        'client-side user list being broken.',

    'max-tick-time': 'The maximum number of milliseconds a single tick may '
        'take before the server watchdog stops the server with the message, A '
        'single server tick took 60.00 seconds (should be max 0.05); '
        'Considering it to be crashed, server will forcibly shutdown. Once '
        'this criteria is met, it calls System.exit(1).',

    'max-world-size': 'This sets the maximum possible size in blocks, '
        'expressed as a radius, that the world border can obtain. Setting the '
        'world border bigger causes the commands to complete successfully but '
        'the actual border will not move past this block limit. Setting the '
        'max-world-size higher than the default doesn\'t appear to do '
        'anything.',

    'motd': 'This is the message that is displayed in the server list of the '
        'client, below the name.',

    'network-compression-threshold': 'By default it allows packets that are '
        'n-1 bytes big to go normally, but a packet that n bytes or more will '
        'be compressed down. So, lower number means more compression but '
        'compressing small amounts of bytes might actually end up with a '
        'larger result than what went in.',

    'online-mode': 'Server checks connecting players against minecraft\'s '
        'account database. Only set this to false if your server is not '
        'connected to the Internet. Hackers with fake accounts can connect if '
        'this is set to false! If minecraft.net is down or inaccessible, no '
        'players will be able to connect if this is set to true. Setting this '
        'variable to off purposely is called "cracking" a server, and servers '
        'that are presently with online mode off are called "cracked" servers, '
        'allowing players with unlicensed copies of Minecraft to join.',

    'op-permission-level': 'Sets permission level for ops.',

    'player-idle-timeout': 'If non-zero, players are kicked from the server if '
        'they are idle for more than that many minutes.',

    'pvp': 'Enable PvP on the server. Players shooting themselves with arrows '
        'will only receive damage if PvP is enabled.',

    'query.port': 'Sets the port for the query server (see enable-query).',

    'rcon.password': 'Sets the password to rcon.',

    'rcon.port': 'Sets the port to rcon.',

    'resource-pack-hash': '',

    'resource-pack': '',

    'server-ip': 'Set this if you want the server to bind to a particular IP. '
        'It is strongly recommended that you leave server-ip blank!',

    'server-port': 'Changes the port the server is hosting (listening) on. '
        'This port must be forwarded if the server is hosted in a network '
        'using NAT (If you have a home router/firewall).',

    'snooper-enabled': 'Sets whether the server sends snoop data regularly to '
        'http://snoop.minecraft.net.',

    'spawn-animals': 'Determines if animals will be able to spawn.',

    'spawn-monsters': 'Determines if monsters will be spawned.',

    'spawn-npcs': 'Determines if villagers will be spawned.',

    'spawn-protection': 'Determines the radius of the spawn protection. '
        'Setting this to 0 will not disable spawn protection. 0 will protect '
        'the single block at the spawn point. 1 will protect a 3x3 area '
        'centered on the spawn point. 2 will protect 5x5, 3 will protect 7x7, '
        'etc. This option is not generated on the first server start and '
        'appears when the first player joins. If there are no ops set on the '
        'server, the spawn protection will be disabled automatically.',

    'texture-pack': '',

    'view-distance': 'Sets the amount of world data the server sends the '
        'client, measured in chunks in each direction of the player (radius, '
        'not diameter). It determines the server-side viewing distance. (see '
        'Render distance)',

    'white-list': 'Enables a whitelist on the server.',
}

DIFFICULTY_CHOICES = (
    (0, 'Peaceful'),
    (1, 'Easy'),
    (2, 'Normal'),
    (3, 'Hard'),
)

GAMEMODE_CHOICES = (
    (0, 'Survival'),
    (1, 'Creative'),
    (2, 'Adventure'),
    (3, 'Spectator'),
)

LEVEL_TYPE_CHOICES = (
    ('DEFAULT', 'DEFAULT'),
    ('FLAT', 'FLAT'),
    ('LARGEBIOMES', 'LARGEBIOMES'),
    ('AMPLIFIED', 'AMPLIFIED'),
    ('CUSTOMIZED', 'CUSTOMIZED'),
)

OP_PERMISSION_LEVEL_CHOICES = (
    (0, 'can bypass spawn protection', ),
    (1, 'can use /clear, /difficulty, /effect, /gamemode, /gamerule, /give, '
        'and /tp, and can edit command blocks'),
    (2, 'can use /ban, /deop, /kick, and /op'),
    (3, 'can use /stop'),
)


class Server(models.Model):
    """
    Representation of a server for hosting games
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    host = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name


class GameVersion(models.Model):
    """
    Minecraft game version
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    link = models.URLField(max_length=250)
    version = models.CharField(max_length=10)
    jar_name = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s" % self.name


class Player(models.Model):
    """
    Player representation
    """
    name = models.CharField(max_length=128)
    uuid = models.CharField(max_length=128)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return u"%s" % self.name


class Game(models.Model):
    """
    Minecraft game instance
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    # configuration = models.OneToOneField(
    #     GameConfiguration
    # )
    server = models.ForeignKey(Server)
    version = models.ForeignKey(GameVersion)

    # Processed fields
    online = models.BooleanField(default=False)
    online_players = models.IntegerField(default=0)

    def _get_map_url(self):
        return "asdfasdf"

    def _get_player_status(self):
        return ['foo', 'bar']

    def _get_server_status(self):
        return {
            'state': 'online',
            'players_online': 2,
            'health': 'warn'
        }

    def _get_map_preview_url(self):
        return "static/img/map-fpo-sm.png"

    def _get_player_count_string(self):
        return "%s/%s" % (self.online_players, self.gameconfiguration.max_players)

    def _get_online_player_list(self):
        return Player.objects.all()

    def __unicode__(self):
        return u"%s" % self.name

    map_preview_url = property(_get_map_preview_url)
    map_url = property(_get_map_url)
    player_status = property(_get_player_status)
    server_status = property(_get_server_status)
    player_count_string = property(_get_player_count_string)
    online_player_list = property(_get_online_player_list)


class GameConfiguration(models.Model):
    """
    Minecraft game configuration

    For details on the fields see:
    http://minecraft.gamepedia.com/Server.properties
    """

    allow_flight = models.BooleanField(default=False)

    allow_nether = models.BooleanField(default=True)

    announce_player_achievements = models.BooleanField(default=True)

    difficulty = models.IntegerField(default=1, choices=DIFFICULTY_CHOICES)

    enable_command_block = models.BooleanField(default=False)

    enable_query = models.BooleanField(default=False)

    enable_rcon = models.BooleanField(default=False)

    force_gamemode = models.BooleanField(default=False)

    gamemode = models.IntegerField(default=0, choices=GAMEMODE_CHOICES)

    generate_structures = models.BooleanField(default=True)

    generator_settings = models.CharField(
        max_length=300,
        blank=True,
        default=''
    )

    hardcore = models.BooleanField(default=False)

    level_name = models.CharField(max_length=200)

    level_seed = models.CharField(max_length=128, blank=True, default='')

    level_type = models.CharField(
        max_length=128,
        default='DEFAULT',
        choices=LEVEL_TYPE_CHOICES
    )

    max_build_height = models.IntegerField(default=256)

    max_players = models.IntegerField(default=20)

    max_tick_time = models.IntegerField(default=60000)

    max_world_size = models.IntegerField(default=29999984)

    motd = models.CharField(max_length=59, blank=True, default='')

    network_compression_threshold = models.IntegerField(default=256)

    online_mode = models.BooleanField(default=True)

    op_permission_level = models.IntegerField(
        default=4,
        choices=OP_PERMISSION_LEVEL_CHOICES
    )

    player_idle_timeout = models.IntegerField(default=0)

    pvp = models.BooleanField(default=True)

    query_port = models.IntegerField(default=25565)

    rcon_password = models.CharField(max_length=128, blank=True, default='')

    rcon_port = models.IntegerField(default=25575)

    resource_pack_hash = models.CharField(
        max_length=128,
        blank=True,
        default=''
    )

    resource_pack = models.CharField(max_length=128, blank=True, default='')

    server_ip = models.CharField(max_length=15, blank=True, default='')

    server_port = models.IntegerField(default=25565)

    snooper_enabled = models.BooleanField(default=True)

    spawn_animals = models.BooleanField(default=True)

    spawn_monsters = models.BooleanField(default=True)

    spawn_npcs = models.BooleanField(default=True)

    spawn_protection = models.IntegerField(default=16)

    texture_pack = models.CharField(max_length=128, blank=True, default='')

    view_distance = models.IntegerField(
        default=10,
        validators=[
            MaxValueValidator(15),
            MinValueValidator(3)
        ]
    )

    white_list = models.BooleanField(default=False)

    game = models.OneToOneField(Game)

    def __unicode__(self):
        return u"%s" % self.id