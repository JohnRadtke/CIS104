filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

file = open(filename)

hour_count = {}
for line in file:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hour_count[hour] = hour_count.get(hour, 0) + 1

sorted_hours = sorted(hour_count.items())

for hour, count in sorted_hours:
    print(hour, count)