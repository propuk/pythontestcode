year = int(input("Enter year: "))
if year%400 == 0 or year%4 == 0:
    print("LEAP YEAR")
elif year%100 == 0:
    print("NOT LEAP YEAR")
else:
    print("NOT LEAP YEAR")
