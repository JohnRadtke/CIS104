filename = input("Enter a file name: ")
try:
    file = open(filename, "r")
except:
    print("Error: file not found")
    quit()

letter_counts = {}
for line in file:
    line = line.lower()
    for char in line:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

letter_list = []
for letter, count in letter_counts.items():
    letter_list.append((count, letter))

letter_list.sort(reverse=True)

for count, letter in letter_list:
    print(letter, count)