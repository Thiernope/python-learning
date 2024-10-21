myDict = {
    "name": "Thierry",
    "age": 23,
    "color": "yellow"
}
myDict["name"] = "Odilo"
print(myDict)
del myDict["color"]

print(myDict["name"])
print(myDict)
print(len(myDict))
print(myDict.keys())
print(myDict.values())


i = 0
while (i <= 6):
    print(i)
    i+=1

print("....................")

for letters in "Hello":
    print(letters)

items = ["Hi", "Hello", "How are you?"]
for elem in items:
    print(items.index(elem), elem)


my_dict = {
    "id": 12,
    "country": "Bdi",
    "color": "Black"
}


for x in my_dict:
    print(x, "=>", my_dict[x])


elements = ["Thierry", "Jado", "Kamali", "Noel", "Helmet"]

# for elem in elements:
#     print(elem)
#     if(elem == "Noel"):
#         break

for elem in elements:
    if(elem == "Noel"):
        break
    print(elem)

for x in range(2, 6):
    print(x)
else:
    print("done printing the numbers in the range (2,6)")



nums = [[1,2, ["a", ["b"]]], [3,4], [5,6]]
print(nums[0][2][1][0]) # will print "b"

for num in nums:
    for row in num:
        for second_row in row:
            if(type(second_row) == int):
                break
            print(second_row)