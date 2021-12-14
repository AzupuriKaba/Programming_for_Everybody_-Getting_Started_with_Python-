# accepting file from user. For simplicity, ensure that data file & py are in same folder
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
counts = dict()

#creating a list from each line stating with "From"
for line in fh:
    # Guardian pair to prevent empty lines from causing Traceback
    if line == '':
        continue
    if line.startswith("From "):
        words = line.split(':')
        # Guardian line to prevent short lines from causing problems
        if len(words) < 1 or words[0] == 'From':
            continue
        else:
            print(words)
# Double splitting to obtain date only
        second_split = words[0].split()
        parts = second_split[-1:]

# Creating a histogram (dictionaries) of all possible items in parts
        for part in parts:
            counts[part] = counts.get(part, 0) + 1
#creating a list of tuples within the dictionary parts
for key,value in counts.items():
    newpair = (key, value)
    lst.append(newpair)
lst = sorted(lst)
for key,value in lst:
    print(key, value)
