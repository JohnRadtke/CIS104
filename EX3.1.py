hours = input("Enter Hours:")
rate = input("Enter Rate:")
fh = float(hours)
fr = float(rate)
if fh > 40 :
    # print("Overtime")
    reg= fr * fh 
    otp = (fh-40.0)*(fr*0.5)
    xp = reg + otp
    print(xp)
else:
   # print("Regular")
    xp= fh * fr 
    print(xp)
