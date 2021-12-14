counts = dict()
name = input("Enter file:")
handle = open(name)
for line in handle:
    if line == "":
        continue
    if line.startswith("From"):
        words = line.split()
        if len(words) < 1 or words[0] != "from":
            continue
        print(words[1])

        #for name in sender_name

        #counts[sender_name] = counts.get(sender_name, 0) + 1
#print(counts)
#sender_name = words[1]

        #for name in sender_name:
            #counts[name] = counts.get(name, 0) + 1
#print(counts)
