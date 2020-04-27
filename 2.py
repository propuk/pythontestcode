sale = float(input("Enter Sale Amount:"))
if sale <= 5000:
    discount = sale * 0.05
    netpay = sale - discount
    print("Discount:",discount)
    print("Net Pay:",netpay)
if sale >= 5000 and sale <= 10000:
    discount = sale * 0.1
    netpay = sale - discount
    print("Discount:", discount)
    print("Net Pay:", netpay)
if sale >= 10000 and sale <= 15000:
    discount = sale * 0.2
    netpay = sale - discount
    print("Discount:", discount)
    print("Net Pay:", netpay)
if sale > 15000:
    discount = sale * 0.3
    netpay = sale - discount
    print("Discount:", discount)
    print("Net Pay:", netpay)