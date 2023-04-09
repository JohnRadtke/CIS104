import re

filename = input("Enter file name:")
total = 0
count = 0

with open(filename) as file:
    for line in file:
        line = line.rstrip()
        nums = re.findall('^New Revision: ([0-9]+)', line)
        if len(nums) > 0:
            total += int(nums[0])
            count += 1

if count > 0:
    avg = int(total / count)
    print(avg)
else:
    print("No matching lines found")