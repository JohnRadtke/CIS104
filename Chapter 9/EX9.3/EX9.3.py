filename = input("Enter the filename: ")
histogram = {}
with open(filename) as f:
    for line in f:
        if line.startswith("From "):
            email = line.split()[1]
            histogram[email] = histogram.get(email, 0) + 1
for email, count in histogram.items():
    print(email, count)