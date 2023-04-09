filename = input('Enter file name: ')

try:
    with open(filename) as file:
        addresses = {}
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                addresses[email] = addresses.get(email, 0) + 1

        if addresses:
            most_messages = max(addresses, key=addresses.get)
            print(most_messages, addresses[most_messages])
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")