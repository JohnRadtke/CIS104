import re

x = input("file name:")
with open(x, 'r') as file:
    integers = re.findall('[0-9]+', file.read())
    total = sum(map(int, integers))

print(total)