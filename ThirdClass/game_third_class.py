inventrory = ["axe", "dagger"]
#0=str  1=dex 2=int 3=hp
skills = [10,10,10,100]
game_over = False

while not game_over:

    while True:

        print("str:", skills[0])
        print("dex:", skills[1])
        print("int:", skills[2])
        print("hp:", skills[3])
        userinput = input("oh dear.do you want to fight?").lower()

        if userinput in ["y","ok","yes","sure"]:

            print(inventrory)
            userinput= input("what item do you want to fight with?")

            if userinput in inventrory:
                print("%s is a great choise" % userinput)

                if userinput == "axe":
                    skills[3] -= 10

                else:
                    skills[3] -= 15
                print("hp:", skills[3])
                if skills[3] == 0:
                    game_over = True
                    break

        print("you found a chest")
        userinput = input("do you want to open it?")

        if userinput in ["y","ok","yes","sure"]:
            print("you opened the chest and found a sword and a book")

            userinput = input("you can only take one, what item do you want?").lower()
            if userinput in ["sword","book"]:
                if userinput == "book":
                    skills[2] += 1
                    print("your int is now:", skills[2])
                inventrory.append(userinput)
                print("the %s was added to your invertory" % userinput)

                print(inventrory)

    print("game over")
