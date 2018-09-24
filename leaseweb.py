#!/usr/bin/env python

# coding: utf-8

# Copyright (c) 2018 Sig-I/O Automatisering
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the software. If not, see <http://www.gnu.org/licenses/>.

'''a dynamic Ansible inventory source based on the LeaseWeb v2 API'''

import argparse
import requests
import json
import os
import sys

apikey = os.environ['LEASEWEB_API_KEY']

url = 'https://api.leaseweb.com/cloud/v2/virtualServers'
headers = {'X-LSW-Auth': apikey}

req = requests.get(url, headers=headers)

content = req.content
content = json.loads(content)
output = {}
names = []
networks = {}

for entry in content['virtualServers']:
    # Find/replace '--' in hostname to '.', so we can have the actual hostname
    if ( entry['reference'] != "" )
      newname = entry['reference']
    else
      newname = entry['name']
    names.append(newname)

    networks[newname] = {
            'ansible_host': entry['ips'][0]['ip'],
            'leaseweb_vars': entry
        }

output['leaseweb'] = names
output['_meta'] = {'hostvars': {}}

for n in names:
    output['_meta']['hostvars'] = networks


print(json.dumps(output))

