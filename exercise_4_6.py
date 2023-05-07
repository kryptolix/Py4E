def computepay(h, r):
    if h > 40 :
        h = h-40
        pay = 40 * r + h * r * 1.5
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print("Pay", p)
