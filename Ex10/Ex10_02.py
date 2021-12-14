fname = input('Enter a file name:')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print(line)
    #if line == '':
        #continue
    #if line.startswith('From'):
        #words = line.split(':')
        #print(words[0])
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
