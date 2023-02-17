def computegrade(score):
    floatscore = float(score)
    if floatscore < 0.0 or floatscore > 1.0:
        print("Error")
    elif floatscore >= 0.9:
        print("A")
    elif floatscore >= 0.8:
        print("B")
    elif floatscore >= 0.7:
        print("C")
    elif floatscore >= 0.6:
        print("D")
    else:
        print("F")

score = input("Enter a score between 0.0 and 1.0: ")
computegrade(score)
