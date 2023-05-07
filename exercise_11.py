import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1401885.txt"
handle = open(name)
numlist = list()

for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y) < 1:
        continue
    for number in y:
        num = int(number)
        numlist.append(num)

result = sum(numlist)
print(result)
