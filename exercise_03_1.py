hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h <= 40 :
    pay = h * r
else :
    overtime = h - 40
    pay = 40 * r + overtime * r * 1.5
print(pay)
