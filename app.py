import math


num = 897
num2 = str(num)

print(type(num))
print(type(num2))

print("...........")
print(isinstance(num, int))
print(isinstance(num2, str))

print("...........")
num3 = -5
print(num3)
print(abs(-5))
print(max(3,4,56))
print(min(3,4,56))
print(round(10.5))
print(bin(23345))

print(math.ceil(2.1))
print(math.floor(2.9))
print(math.trunc(2.333))
print(math.sqrt(4))

# sentence = input("Type your sentence: ")
# print("Your sentence is: ", sentence)

# word1 = input("Which word you want to replace: ")
# word2 = input("which word you want to replace it with: ")
# print("Result: ", sentence.replace(word1, word2))


fruits = ["Apple", "Banana", True, 2, "strawberries"]
fruits[0] = "Onion"
print(fruits[0])
print(type(fruits[-3]))

fruits2 = list(("XX", 3, "Hola", True))
print(fruits2[0])

fruits.extend(fruits2)
print(fruits)

fruits2.append("!!!")
print(fruits2)

fruits2.insert(1, "UUUUU")
print(fruits2)

fruits2.remove("UUUUU")
print(fruits2)
del fruits2[1]
print(fruits2)
fruits


textList = [1, 2, 3]
newTextList = ["baby", "cousin", "baby"]

combinedList = textList[:1] + newTextList + textList[1:]
print(combinedList)


print(combinedList.index("baby"))

print(combinedList.count("baby"))

numx = [3,5,2,5]
numx.sort()
numx.reverse()
print(numx)

numttt = numx.copy()
print(numttt)

# del numttt


#Tuples

three_numbers = (1,2, "home",3)
print("XXXX", three_numbers)
print(type(three_numbers))
print(three_numbers.count(2))

myTuple = tuple((23,4,5))
print(myTuple)

