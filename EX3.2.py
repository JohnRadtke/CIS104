hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("error,please enter numeric value")
if fh > 40 :
    # print("Overtime")
    reg= fr * fh 
    otp = (fh-40.0)*(fr*0.5)
    xp = reg + otp
    print(xp)
else:
   # print("Regular")
    xp= fh * fr 
    print(ep)
