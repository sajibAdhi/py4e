
def computepay(h, r):
    if(h > 40):
        result = (40*r)+((h-40)*r*1.5)
    else:
        result = h*r
    return result


hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)
