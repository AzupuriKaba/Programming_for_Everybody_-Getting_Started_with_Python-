fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#inp = fh.read()
#index = 0
for line in fh:
    #line = line.rstrip()
    words = line.split()
    #lst.append(words)
    #if check is True:
    for word in words:
        if word not in lst:
            lst.append(word)
        #if check is True:
            #continue
        #lst.extend(word)
#print(line.rstrip())
lst.sort()
print(lst)
