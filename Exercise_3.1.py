hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
ot = 0
gross_pay = 0

if h > 40 :
    gross_pay = 40 * r
    ot = (h - 40) * (1.5 * r)
    gross_pay = gross_pay + ot
else:
    gross_pay = h * r
print(gross_pay)