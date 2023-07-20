import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    sum = 0
    
    print('Retrieving', address)
    rawjson = urllib.request.urlopen(address, context=ctx).read()

    tree = json.loads(rawjson)
    print('Retrieving', len(rawjson), 'characters')
          
    comms = tree['comments']
    print('Count:', len(comms))

    for item in comms:
         sum += int(item['count'])

    print('Sum:', sum)
