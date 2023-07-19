import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
    rawxml = urllib.request.urlopen(address, context=ctx).read()

    tree = ET.fromstring(rawxml)
    sum = 0
    counts = tree.findall('.//count')
    for item in counts:
        sum += int(item.text)

    print(sum)
