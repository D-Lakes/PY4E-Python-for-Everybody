def computepay(h, r):
    ot = 0
    rp = 0
    gross_pay = 0
    if h > 40 and r > 0 :
        ot = (h - 40) * (1.5 * r)
        rp = (40 * r)
        gross_pay = ot + rp
    elif h > 0 and r > 0 :
        gross_pay = h * r
    else:
        return "Enter valid hours and pay rates"
    return gross_pay

hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")
hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print("Pay", p)