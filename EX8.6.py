my_nums = []
while True:
    str_val = input("Enter a number")
    if str_val == 'done':
        break
    try :
        val = float(str_val)
    except:
        print ("Invalid input")
        continue
    my_nums.append(val)
print(min(my_nums),max(my_nums))
