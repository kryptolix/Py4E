# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input prompts
url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)

rep = 0

while rep <= int(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
    tags = soup('a')

# Look at the parts of a tag
    print('Retrieving: ' + url)
    
#    print('TAG:', tags[int(position)-1])
#    print('URL:', tags[int(position)-1].get('href', None))
#    print('Contents:', tags[int(position)-1].contents[0])
#    print('Attrs:', tags[int(position)-1].attrs)
    url = tags[int(position)-1].get('href', None)
    rep += 1
