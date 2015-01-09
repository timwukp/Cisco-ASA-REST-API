#
# Generated ASA REST API sample script
#

import base64
import json
import sys
import urllib2
import string

while True:

    objectid = raw_input('Please enter the rule ID which you want to delete: ')

    server = "https://YOUR ASA MANAGEMENT IP ADDRESS"

    username = "cisco"
    if len(sys.argv) > 1:
        username = sys.argv[1]
    password = "cisco"
    if len(sys.argv) > 2:
        password = sys.argv[2]


    headers = {'Content-Type': 'application/json'}

    api_path = "/api/access/global/rules/"    # param
    url = server + api_path + objectid
    f = None



    # GET OPERATION


    req = urllib2.Request(url, None, headers)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)
    try:
        f = urllib2.urlopen(req)
        status_code = f.getcode()
        if (status_code != 200):
            print 'Error in get. Got status code: '+status_code
        resp = f.read()
        json_resp = json.loads(resp)
        print json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': '))
    finally:
        if f:  f.close()


    YesorNo=raw_input('Do you want to delete it?(Y/N): ')
    if YesorNo=='N':
        print('Bye-bye')
        break



    # DELETE OPERATION

    req = urllib2.Request(url, None, headers)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)   
    req.get_method = lambda: 'DELETE'

    try:
        f = urllib2.urlopen(req)
        status_code = f.getcode()
        print "Status code is "+str(status_code)
        if status_code == 204:
            print "DELETE operation was successful"
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

    YesorNo=raw_input('Do you want to continue?(Y/N): ')
    if YesorNo=='N':
        print('Bye-bye')
        break

    
