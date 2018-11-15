#exercise 1
myDict = {i: i ** 2 for i in range(1,21)}
print(myDict)

#exercise 3
room_items = {"item1": {"Name": "Lamp", "Colour": "Red"}, "item2": {"Name": "Table", "Colour": "Brown", "Type": 0}, "item3": {"Name": "Lamp", "Colour": "Red"}, "item4": {"Name": "Chair", "Colour": "Green", "Type": 1}}
room_items_final={}
for item in room_items:
    checker = False
    for tester in room_items_final:
        if room_items[item] == room_items_final[tester]:
            checker = True
    if checker == False:
        room_items_final[item] = room_items[item]
print(room_items_final)

#exercise 3
# i have done the same as exercise 3 during class in the file game_third_class.py