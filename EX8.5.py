fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
