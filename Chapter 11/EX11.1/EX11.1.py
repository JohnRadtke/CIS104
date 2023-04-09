import re

filename = input("Enter file name: ")
regex = input("Enter a regular expression: ")
count = 0

with open(filename) as file:
    for line in file:
        line = line.rstrip()
        if re.search(regex, line):
            count += 1

print(f"{filename} had {count} lines that matched {regex}")