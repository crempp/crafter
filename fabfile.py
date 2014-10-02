import os

from fabric.api import local
from fabric.context_managers import cd

CRAFTER_BASE_PATH = os.path.dirname(os.path.realpath(__file__))
SERVER_JAR_PATH = os.path.join(CRAFTER_BASE_PATH, 'bin/server-jars')
DIRECTORY = os.path.join(CRAFTER_BASE_PATH, 'games/')


def start(game_id):
    # The -Xms option sets the initial and minimum Java heap size. The Java
    # heap (the "heap") is the part of the memory where blocks of memory are
    # allocated to objects and freed during garbage collection.
    #
    # Note:	-Xms does not limit the total amount of memory that the JVM can use.
    xms_ram = '512M'

    # This option sets the maximum Java heap size. The Java heap (the "heap")
    # is the part of the memory where blocks of memory are allocated to objects
    # and freed during garbage collection. Depending upon the kind of
    # operating system you are running, the maximum value you can set for the
    # Java heap can vary.
    #
    # Note:	-Xmx does not limit the total amount of memory that the JVM can use.
    xmx_ram = '512M'

    version = "1.8"

    server_jar = "%s/minecraft_server.%s.jar" % (SERVER_JAR_PATH, version)

    game_path = os.path.join(DIRECTORY, game_id)
    local('mkdir %s' % game_path)

    with cd(game_path):
        #local('java -Xms%s -Xmx%s -jar %s nogui' % (xms_ram, xmx_ram, server_jar))
        local('ls')