filename = input("Enter the filename: ")
histogram = {}
with open(filename) as f:
    for line in f:
        if line.startswith("From "):
            email = line.split()[1]
            histogram[email] = histogram.get(email, 0) + 1

most_messages = None
most_count = None
for email, count in histogram.items():
    if most_count is None or count > most_count:
        most_messages = email
        most_count = count

print ("The email address with the most messages is", most_messages,)
print ( "They sent", most_count, "messages.")