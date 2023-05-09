import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#start_url = input("Enter URL: ")
#count_input = input("Enter count: ")
#position_input = input("Enter position: ")
#count = 0

#while int(count) <= int(count_input):
#    count += 1
#    f_hand = urllib.request.urlopen(start_url)
#    print("Retrieving: " + str(start_url))
#    position = 0
#    for line in f_hand:
#        linestring = line.decode().strip()
#        if "href" in linestring:
#            position += 1
#            if position == int(position_input):
#                test = linestring.split('>')
#                url_list = test[1].split('"')
#                start_url = str(url_list[1])

