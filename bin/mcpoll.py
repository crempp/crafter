#!/usr/bin/env python
"""
Mincraft server polling script and data aggregator

This script
* polls the Minecraft servers for their status
* parses the server.properties file
* assembles all this data into a single JSON file for consumption

It is intended that this file be run by a cron script (such as /etc/crontab).
The following is a sample entry for cron (runs every two minutes)
  02 * * * * /path/to/mcpoll.py
  
"""

OUTPUT_PATH = '/srv/crafter.lapinlabs.com/data/servers.json'
TIMEOUT = 1
RETRIES = 2

import sys
from pprint import pprint
import socket
import json
from minecraft_query import MinecraftQuery
from mcconfig import config

def parse_config(path):
    f = open(path + '/server.properties', 'r')
    
    config = {}
    
    for line in f:
        if '#' == line[0]: continue
        
        parts = line.replace("\n", '').split('=')
        
        if 2 != len(parts): continue
        
        config[parts[0]] = parts[1]
    
    return config

def poll(server):
    print 'checking on %s:%s...'%(server['host'], server['port'])
    
    config = parse_config(server['path']);
    
    try:
        query = MinecraftQuery(server['host'], server['port'],
                               timeout=TIMEOUT,
                               retries=RETRIES)
        server_data = query.get_rules()
    except socket.error as e:
        print 'socket exception caught:', e.message
        print 'Server is down or unreachable.'
        server_data = {}

    server_data['id'] = server['id']
    
    return server_data
    
if __name__ == '__main__':
    data = config.copy()
    
    for i, server in enumerate(config['servers']):
        server_properties = parse_config(server['path'])
        data['servers'][i].update({
            #'id': server['id'],
            'name': server_properties['level-name'],
            #'host': server['host'],
            #'path': server['path'],
            #'map': server['map'],
            #'description': server['description'],
            'status': poll(server),
            'config': server_properties,
        })

    serialized = json.dumps(data)
        
    #print 'data:'
    #print(serialized)

    f = open(OUTPUT_PATH, 'w')
    f.write(serialized)
