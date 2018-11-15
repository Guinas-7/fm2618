x=["mix", "xyz", "apple", "xanadu","rovio"]
new_list_a = []
new_list_b = []

for word in x:
    if word[0] == "x":
        new_list_a.append(word)
    else:
        new_list_b.append(word)

print(sorted(new_list_a) + (sorted(new_list_b)))



print ([x**2 for x in range(10)])

t= (2,3)
print(t)

tuple_list = [(), (), ('',), ("a", "b"), ("a", "b", "c"), ("d")]

print([x for x in tuple_list if x])


my_dict = {"Name":"Rex","Age":7,"Pedigree":"Rotweiler"}

my_dict["Age"]=8

print(my_dict["Name"])
print(my_dict["Age"])
print(my_dict["Pedigree"])


dict_helms = {}

dict_inventory = {"str":10,"dex":7,"hp":100,"sword":"excalibur","helm":dict_helms["greathelm2"]}

