import urllib
import urllib2,base64
import json
from pprint import pprint

username = 'cisco'
password = 'cisco'

BaseURL = 'https://YOUR ASA MANAGEMENT IP ADDRESS/api'

OnDemandQueryURL = BaseURL+'/cli'

Showconfig = { "commands": [ "show configuration", "write", "show configuration" ] }

req = urllib2.Request(OnDemandQueryURL,json.dumps(Showconfig), {'Content-Type': 'application/json'})

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string) 

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
