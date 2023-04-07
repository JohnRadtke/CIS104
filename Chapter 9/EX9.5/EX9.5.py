filename = input("Enter a file name: ")
domain_counts = {}

with open(filename, 'r') as f:
    for line in f:
        if line.startswith('From '):
            domain = line.split()[1].split('@')[1]
            if domain in domain_counts:
                domain_counts[domain] += 1
            else:
                domain_counts[domain] = 1

print(domain_counts)