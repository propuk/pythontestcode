def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
num = int(input("Enter Number : "))
if num < 0:
    print("factorial cannot be found.")
else:
    print("Factorial of ",num," is ",factorial(num))
