for i in "python":
    if i != "t":
        print(i, end="")
print()

myList = ["hello", "my", "name", "is", "Guilherme"]
for i in myList:
    print(i, end=" ")

myList2 = [1, 2, [3, 4, 5]]
print(myList2[2][1])


x = 0
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]
for i in words:
    if (len(i) >= 2) & (i[0] == i[-1]):
        x += 1
print(x)


numbers = [2, 3, 5, 7, 66, 89, 134]
newList = []
y = int(input("pick a number: "))
for i in numbers:
    if i < y:
        newList.append(i)
print(newList)