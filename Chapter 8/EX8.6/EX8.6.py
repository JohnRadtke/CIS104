my_nums = []

while True:
    str_val = input("Enter a number: ")
    if str_val == 'done':
        break
    try :
        val = float(str_val)
    except:
        print ("Invalid input")
        continue
    my_nums.append(val)

if my_nums:
    print("Min", min(my_nums))
    print("Max:", max(my_nums))
else:
    print("No values were entered.")