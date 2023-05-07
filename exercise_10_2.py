name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
time = list()
counts = dict()
tempcount = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    lst = line.split()
    if len(lst) <= 2:
        continue
    tmp = lst[5]
    time = tmp.split(":")
    counts[time[0]] = counts.get(time[0], 0) + 1

for key, val in sorted(counts.items()):
    print(key, val)
