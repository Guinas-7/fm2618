weapons = {"sword": 5, "dagger":3}
fightMode = False

while True:

    usr = input("Where to? ")

    if usr in ["n", "north"]:
        print("Oh this looks like trouble!")

        usr = input("Will you fight?").lower()
        if usr in ["yes", "y", "hell yeah"]:
            fightMode = True
        else:
            continue

        if fightMode:
            usr = input("which weapon you want to use: ")
            weaponIsValid = False
            while weaponIsValid == False:

                usrp = usr.split(" ")  # list

                for word in usrp:
                    if weaponIsValid== False:
                        if word in weapons:
                                print("With the %s you do"%word , weapons[word],"damage. On we go!")
                                weaponIsValid = True

                        else:
                            usr = input("which weapon?")
    elif usr in ["s", "w", "e", "south", "west", "east"]:
        print("Nothing there")
    else:
        print("This is not a valid direction")

    # Further code for the fight ...




