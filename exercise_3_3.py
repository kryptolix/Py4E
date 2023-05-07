score = input("Enter Score: ")
try:
    score = float(score)
except:
    score = 2

if score > 1.0:
    print("Not a number or out of range!")
elif score < 0.0:
    print("Out of range!")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
