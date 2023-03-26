fname = input("Enter file name:")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        line = float(line[21:])
        total = line + total

average = total / count
print("Average spam confidence:", average)