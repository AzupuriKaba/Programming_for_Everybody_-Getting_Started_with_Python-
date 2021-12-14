# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp_upper = inp.upper()
print(inp_upper.rstrip())
