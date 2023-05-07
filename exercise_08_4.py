fname = input("Enter file name: ")
fh = open(fname)
lst = list()
test = list()
for line in fh:
    line = line.rstrip()
    test = line.split()
    for w in test:
        if w in lst:
            continue
        else:
            lst.append(w)
lst.sort()
print(lst)
