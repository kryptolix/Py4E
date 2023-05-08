import urllib.request
import urllib.parse
import urllib.error

start_url = input("Enter URL: ")
count_input = input("Enter count: ")
position_input = input("Enter position: ")
count = 0

while int(count) <= int(count_input):
    count += 1
    f_hand = urllib.request.urlopen(start_url)
    print("Retrieving: " + str(start_url))
    position = 0
    for line in f_hand:
        linestring = line.decode().strip()
        if "href" in linestring:
            position += 1
            if position == int(position_input):
                test = linestring.split('>')
                url_list = test[1].split('"')
                start_url = str(url_list[1])
