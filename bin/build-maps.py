#!/usr/bin/env python
'''
# Minecraft version
VERSION=1.7.9

CLIENT_PATH="~/.minecraft/versions"

SERVER_PATH[0]="/srv/minecraft.65/Land of the Unnamed Wise Turtles"

OUTPUT_PATH[0]="/var/www/crafter.lapinlabs.com/webroot/maps/65"


# Download the client for the textures
if [ ! -d $CLIENT_PATH/${VERSION}/ ]; then
    
fi

overviewer.py $SERVER_PATH 

overviewer.py "/srv/minecraft.64/world" "/var/www/crafter.lapinlabs.com/webroot/maps/64"
'''

import json
import os.path
import shutil
from os import system
from os import mkdir
from datetime import datetime

DATA_PATH = '/var/www/crafter.lapinlabs.com/data/servers.json'

CLIENT_PATH = '/var/www/crafter.lapinlabs.com/data'

config = json.load(open(DATA_PATH, 'r'))

for server in config['servers']:
    print('Building map [%s]' % server['name'])
    
    # Download the required version of the client
    print('  Checking for correct client version..')
    version = server['status']['version']
    if not os.path.isfile('%s/%s/%s.jar' % (CLIENT_PATH, version, version)):
        print('    Downloading Minecraft client %s..' % version)
        system('wget https://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.jar -P %s/%s/' % (version, version, CLIENT_PATH, version))
    else:
        print('    OK')

# Run overviewer
start = datetime.now()
print('  Running Overviewer build [started %s]' % start.strftime("%H:%M:%s"))

# TODO: Move the map config path into a base setting. For now we're grabbing it from the first element
system('overviewer.py --config "%s"' % (config['map']['config']))

end = datetime.now()
print('  Finished build [total time %s]' % (end - start))
    
    

