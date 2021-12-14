fname = input("Enter file name: ")
fh = open(fname)
lst = list()
counts = dict()
largest_count = None
frequent_word = None

#creating a list
for line in fh:
    if line == '':
        continue
    if line.startswith("From"):
        words = line.split()
        #print(words)
        if len(words) < 1 or words[0] != "From":
            continue
        lst.append(words[1])
#print(lst)
    #print(lst.append(words[1]))
    #counting total number of different senders
for sender_name in lst:
    counts[sender_name] = counts.get(sender_name, 0) + 1
print(counts)
#creating histgram
for sender_name,count in counts.items():
    if largest_count is None or count > largest_count:
        largest_count = count
        frequent_word = sender_name
print(frequent_word, largest_count)
#print(counts)
    #print(lst.append(user))
#print(lst)
#print("ghana")
