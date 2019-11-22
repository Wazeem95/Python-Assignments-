num1 = int(input("Enter Your First Number"))
opreator = input("Enter Your Opreator")
num2 = int(input("Enter Your First Number"))

if opreator == '+':
    result = num1 + num2
    print("Addition of ",num1," & ",num2," is ", result)
elif opreator == '-':
    result = num1 - num2
    print("Subtraction of ",num1," & ",num2," is ", result)
elif opreator == '*':
    result = num1 * num2
    print("Multiplication of ",num1," & ",num2," is ", result)
elif opreator == '/':
    result = num1 / num2
    print("Division of ",num1," & ",num2," is ", result)
elif opreator == '**':
    result = num1 ** num2
    print("Power of ",num1, " is ", result)