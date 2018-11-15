#exercise 1
a_list = [3, 5, 6, 12]
#1
print(a_list[0])
#2
print(a_list[1:4])
#3
print(a_list[::-1])
#4
b_list = []
for i in a_list:
    b_list.append(i * 3)
print(b_list)
#5
b_list = []
for i in a_list:
    b_list.append(i %6 ==0)
print(b_list)

#exercise 2
c_list =[int(x) for x in input("please insert a list of numbers separated with spaces").split()]
print(c_list)

#exercise 3
myList = ["axe", "dagger", "oranges"]
myFinalList=[]
[myFinalList.extend(["*",item]) for item in myList]
print(myFinalList)