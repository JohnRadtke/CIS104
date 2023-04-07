filename = input("Enter the filename: ")
counts = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0}
with open(filename, "r") as f:
    for line in f:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 2:
                day = words[2]
                if day in counts:
                    counts[day] += 1
for day, count in counts.items():
    print(day, count)