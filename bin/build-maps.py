#!/usr/bin/env python
''' Build maps using overviewer for all servers in the servers.json file'''

import json
import os.path
import shutil
from os import system
from os import mkdir
from datetime import datetime

DATA_PATH = '/srv/crafter.lapinlabs.com/data/servers.json'

CLIENT_PATH = '/srv/crafter.lapinlabs.com/data'

config = json.load(open(DATA_PATH, 'r'))

for server in config['servers']:
    print('Building map [%s]' % server['name'])
    
    # Download the required version of the client
    print('  Checking for correct client version..')
    
    try:
        version = server['status']['version']
    except:
        # No version probably means it's not running, skip
        # TODO: handle this in a cleaner way
        print("    no version info, is the server down? Skipping.")
        continue
    
    if not os.path.isfile('%s/%s/%s.jar' % (CLIENT_PATH, version, version)):
        print('    Downloading Minecraft client %s..' % version)
        system('wget https://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.jar -P %s/%s/' % (version, version, CLIENT_PATH, version))
    else:
        print('    OK')

    # Run overviewer
    start = datetime.now()
    print('  Running Overviewer build [started %s]' % start.strftime("%H:%M:%s"))

    mapconfig = '%s/overviewer.config' % server['path']
    cmd = 'export MAP="%s"; overviewer.py --config "%s"' % (server['name'], mapconfig)
    print(cmd)
    system(cmd)

    end = datetime.now()
    print('  Finished build [total time %s]' % (end - start))
    
   
