count = 0
total = 0
minimum = None
maximum = None

while True:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        break
    
    try:
        number = float(user_input)
        count += 1
        total += number
        
        if minimum is None or number < minimum:
            minimum = number
            
        if maximum is None or number > maximum:
            maximum = number
        
    except:
        print("Invalid input")
        continue

if count > 0:
    print(total, count, minimum, maximum)
else:
    print("No valid numbers entered.")
