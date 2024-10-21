countr_file = open("countries.txt", "r")

# print(countr_file.readlines())

lines = countr_file.readlines()
print(type(lines))
for line in lines:
    print("Line", lines.index(line), "=>", line)

countr_file.close()


new_file = open("fruits.txt", "w")

new_file.writelines(
    "Orange"
    "Banana"
    "Apple"
    )

new_file.close()


readFile = open("fruits.txt", "r")
print(readFile.readlines())

readFile.close()


print(open("fruits.txt", "r+").write("00000_---))))00000"))

print(open("fruits.txt", "r").readlines())




