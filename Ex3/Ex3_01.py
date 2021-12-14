hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

if h <= 40:
    pay = r * h
if h > 40:
    pay = (1.5 * r * (h - 40)) + (r * 40)
print(pay)
