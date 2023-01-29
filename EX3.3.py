score = (input("Enter a score between 0.0 and 1.0: "))
floatscore = float(score)
if floatscore < 0.0 or floatscore > 1.0:
    print("Error")
if floatscore > 0.9:
    grade = "A"
elif floatscore > 0.8:
    grade = "B"
elif floatscore > 0.7:
    grade = "C"
elif floatscore > 0.6:
    grade = "D"
else:
    grade = "F"
print(grade)
