num1 = int(input("FirstNumber: "))
operator = input("Enter operation: ")
num2 = int(input("secondNumber: "))

def calc(num1, num2, operator):
    if(operator == "*"):
        return num1 * num2
    elif(operator == "+"):
        return num1 + num2
    elif(operator == "/"):
        return num1 / num2
    elif(operator == "-"):
        return num1 - num2
    else:
        return "Invalid Operation"

result = calc(num1, num2, operator)
print(result)