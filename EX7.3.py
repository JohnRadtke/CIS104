fname = input("Enter file name:")
if fname == "na na boo boo":
    print("Na Na Boo Boo To You - You have been punk'd!")
else:
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
