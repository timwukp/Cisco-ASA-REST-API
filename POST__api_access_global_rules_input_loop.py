#
# Generated ASA REST API sample script
#

import base64
import json
import sys
import urllib2
import getpass

print ('Please login first')

username = raw_input('Username: ')
# username = "cisco"
if len(sys.argv) > 1:
    username = sys.argv[1]

password = getpass.getpass('Password: ')
# password = "cisco"
if len(sys.argv) > 2:
    password = sys.argv[2]

print (' ')

while True:
    print ('Please select the type of source IPv4 address')
    print ('e.g. 121.1.10.0/24 is a network address, 1.1.1.1 is a host address')
    print ('0 for network,1 for host')
    sourceAddressType = raw_input ('Please select the number: ')
    if sourceAddressType=='0':
        sourceAddressKind="IPv4Network"
        sourceAddress = raw_input('Please enter source IPv4 subnet/mask: ')
        break
    if sourceAddressType=='1':
        sourceAddressKind="IPv4Address"
        sourceAddress = raw_input('Please enter source IPv4 host address: ')
        break
    else:
        print ('Sorry, it is a wrong number, please enter again')
        print ('')
        True

while True:
    print ('Please select the type of destination IPv4 address')
    print ('0 for network,1 for host')
    destinationAddressType = raw_input ('Please select the number: ')
    if destinationAddressType=='0':
        destinationAddressKind="IPv4Network"
        destinationAddress = raw_input('Please enter destination IPv4 subnet/mask: ')
        break
    if destinationAddressType=='1':
        destinationAddressKind="IPv4Address"
        destinationAddress = raw_input('Please enter destination IPv4 host address: ')
        break
    else:
        print ('Sorry, it is a wrong number, please enter again')
        print ('')
        True


while True:
    print ('Please select servicve type by the number')
    print ('1 for IP, 2 for tcp, 3 for udp, 4 for specific number')
    serviceType = raw_input('Please select the number: ')
    if serviceType=='1':
        serviceKind="NetworkProtocol"
        sourceServiceValue="ip"
        destinationServiceValue="ip"
        break
    if serviceType=='2':
        serviceKind="NetworkProtocol"
        sourceServiceValue="tcp"
        destinationServiceValue="tcp"
        break
    if serviceType=='3':
        serviceKind="NetworkProtocol"
        sourceServiceValue="udp"
        destinationServiceValue="udp"
        break
    if serviceType=='4':
        serviceKind="TcpUdpService"
        print ('Please specify the port number or range in the following format')
        print ('e.g. tcp/12345-23456 or udp/1234 or tcp/http')
        sourceServiceValue = raw_input('Please enter source number: ')
        destinationServiceValue = raw_input('Please enter destination number: ')
        break
    else:
        print ('Sorry, it is a wrong number, please enter again')
        print ('')
        True

while True:
    print ('Please chose permit or deny action')
    print ('0 for permit, 1 for deny')
    trueORfalse = raw_input('Please select the number: ')
    if trueORfalse=='0':
        trueORfalse="true"
        break
    if trueORfalse=='1':
        trueORfalse="false"
        break
    else:
        print ('Sorry, it is a worng number, please enter again')
        True

server = "https://YOUR IP ADDRESS"

headers = {'Content-Type': 'application/json'}

api_path = "/api/access/global/rules"    # param
url = server + api_path
f = None

# POST OPERATION
post_data = {
  "sourceService": {
    "kind": serviceKind,
    "value": sourceServiceValue
  },
  "destinationAddress": {
    "kind": destinationAddressKind,
    "value": destinationAddress
  },
  
  "remarks": [],
  "destinationService": {
    "kind": serviceKind,
    "value": destinationServiceValue
  },
  "permit": trueORfalse,
  "active": "true",
  "position": "1",
  "sourceAddress": {
    "kind": sourceAddressKind,
    "value": sourceAddress
  }
}

req = urllib2.Request(url, json.dumps(post_data), headers)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)   
try:
    f  = urllib2.urlopen(req)
    status_code = f.getcode()
    print "Status code is "+str(status_code)
    if status_code == 201:
        print "Create was successful"
except urllib2.HTTPError, err:
    print "Error received from server. HTTP Status code :"+str(err.code)
    try:
        json_error = json.loads(err.read())
        if json_error:
            print json.dumps(json_error,sort_keys=True,indent=4, separators=(',', ': '))
    except ValueError:
        pass
finally:
    if f:  f.close()






    
