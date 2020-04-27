num1 = float(input("First Number:"))
op = str(input("Operator (+,-,*,/):"))
num2 = float(input("Second Number:"))
if op == "+" :
    result = num1 + num2
    print(str(result))
elif op == "-" :
    result = num1 - num2
    print(str(result))
elif op == "*" :
    result= num1 * num2
    print(str(result))
elif op == "/" :
    result = num1 / num2
    print(str(result))
else:
    print("Error")