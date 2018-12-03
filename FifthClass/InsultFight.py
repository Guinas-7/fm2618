import random
counter = 0
while counter < 3:
    a=random.choice(["You're a scallywag","Flea, Bitten mongrel","I hate you"])
    print(a)
    b = input("Choose a comeback: Lilly livered cod swine, Come merda")

    if a == "You're a scallywag":
        if b == "come merda":
            print("Man, that was cold")
            counter += 1
        else:
            print("You call that a comeback?")

    elif a == "Flea, Bitten mongrel":
        if b == "come merda":
            print("Man, that was cold")
            counter += 1
        else:
            print("You call that a comeback?")

    elif a == "I hate you":
        if b == "come merda":
            print("Man, that was cold")
            counter += 1
        else:
            print("You call that a comeback?")

print("you win")