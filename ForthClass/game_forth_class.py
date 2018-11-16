inventrory = {}
items = ("dagger", "BluePotion","GoldenFeather", "manuscript")
#0=fly ability  1=stealth
skills = [0,0]
game_over = False

while not game_over:

    while True:

        print("fly ability:", skills[0])
        print("stealth:", skills[1])


        print("you found a chest")
        userinput = input("do you want to open it?")

        if userinput in ["y","ok","yes","sure"]:
            print("you opened the chest and found a %s, a %s some %s and a %s" % (items[0], items[1], items[2], items[3]))

            userinput = input("what items do you want?").lower()

            userinputitems = userinput.split(" ")
            for i in userinputitems:
                if i in items:
                    if i ==  items(1) & skills[0]<5:
                        skills[0] =+ 1
                    if i == items(2) & skills[1]<5:
                        skills[1] = + 1
                    if i in inventrory:
                        inventrory[i] = inventrory.get(i) + 1
                    else:
                        inventrory[i] = 1

            print(inventrory)


    print("game over")
