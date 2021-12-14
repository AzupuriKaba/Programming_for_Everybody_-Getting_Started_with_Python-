def computepay(h,r):
    if h <= 40:
        p = h * r
        return(p)
    if h > 40:
        p =(1.5 * r * (h - 40)) + (r *40)
        return(p)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h, r)
print("Pay",p)
