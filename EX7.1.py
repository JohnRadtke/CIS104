fname = input("Enter file name: ")
with open(fname) as fh:
    fh = fh.read()
print(fh.upper())
