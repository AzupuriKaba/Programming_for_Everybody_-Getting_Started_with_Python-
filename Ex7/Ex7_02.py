# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
addup = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    a = len(line)
    b = line.find(":")
    number = float(line[b+1 : a+1])
    #print(line)
    count = count + 1
    addup = addup + number
print("Average spam confidence:", addup/count)
