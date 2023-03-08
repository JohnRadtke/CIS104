fname = input("Enter file name: ")
fh = open(fname)
for lx in fh:
    print(lx.rstrip().upper())
