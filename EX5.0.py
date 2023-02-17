count = 0
total = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        break
    
    try:
        number = float(user_input)
        count += 1
        total += number
    except:
        print("Invalid input")
        continue

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No valid numbers entered.")
