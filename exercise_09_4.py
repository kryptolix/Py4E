name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()

histogram = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    lst = line.split()
    histogram[lst[1]] = histogram.get(lst[1], 0) + 1

bigcount = None
bigword = None
for word, count in histogram.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
