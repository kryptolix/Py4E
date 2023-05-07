# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
numadd = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    ipos = line.find(":")
    numstr = line[ipos+1:]
    numfloat = float(numstr)
    numadd = numadd + numfloat
    spamav = numadd / count
print("Average spam confidence:", spamav)
