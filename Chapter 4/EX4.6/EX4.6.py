def computepay(hours, per_rate_hours):


    if (hours>40):
        pay = hours * per_rate_hours
        overtime = (hours - 40)   * (0.5 * per_rate_hours)
        payment = pay + overtime

    else:
        payment = hours * per_rate_hours
    return payment


hours = input("Enter Hours: ")
per_rate_hours = input("Enter Per Rate Hour: ")

try:
	f_hours= float(hours)
	f_per_rate_hours=float(per_rate_hours)
except:
    print("Error")
    quit()

final_pay = computepay(f_hours, f_per_rate_hours)
print("Pay", final_pay)