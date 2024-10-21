# def greetings_func(a = 4, b = 6):
#     result = str(a)
#     print(type(result))
#     print(a * b)
 
# greetings_func()


# def multArgs_fun(*names):
#     print("Welcome", names)

# multArgs_fun("Thierry", 1, True)

# def add_numbers(num1, num2):
#     if(num1 == num2):
#         return num1 + num2
#     elif(num1 < num2):
#         return "We cannot because first number is small than second number"
#     else:
#         return "We cannot add numbers because they are not equal"
    
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(add_numbers(num1, num2))



# def checkEvenNumber(num):
#     if(num % 2 == 0):
#         return num, "is even number"
#     else:
#         return num, "is odd number"
    
# print(checkEvenNumber(7))


# a = 10
# def checkTruthy():
#     if(a % 5 == 1 or a < 1):
#         return True
#     else:
#         return False

# print(checkTruthy())


b = 2
def check_greater_or_equal():
    return b <= 4
print(check_greater_or_equal())
