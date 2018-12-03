def addition(a,b):
    print(a+b)
addition(int(input("give me a number")),int(input("and now another number")))



def multiplier(a_list):
    b_list=[]
    for i in a_list:
        b_list.append(i * 2)
    return (b_list)

list_input=[1,2,3,4,5,6,7,8,9]
print(multiplier(list_input))
print(multiplier(multiplier(list_input))) #using the output from a function as the input of a function


a=4

def update_local_var():

    a = 17
    print("the value of the var inside is:", a)

update_local_var()
print("the value of the var outside is:", a)




def update_global_var():
    global a
    a = 6
    print("the value of the var inside is:", a)

update_global_var()
print("the value of the var outside is:", a)


def player_name():
    name =  input("what is your name?")
    if name == "rainbow unicorn":
        print("that's the same as mine! :D")
    else:
        print("that's a stupid name! :(")
    return name

print (player_name())



def player_death(CauseOfDeath):
    print("you died from", CauseOfDeath)
    exit()



sword = False
def encouter():
    global sword
    OpenChest = input("You encounter a chest, would you like to open it?")
    if OpenChest == "yes":
        print("You found a sword inside the chest")
        sword = True
    else:
        print("Ok then")
    return


while True:
    DoorChoice = input("you see 3 doors, which one do you want to choose?")
    if DoorChoice == ("door1"):
        encouter()
    elif DoorChoice == ("door2"):
        player_death("falling into a pit of snakes")
    elif DoorChoice == ("door3"):
        FightChoice = input("You encounter Cthulu, do you wish to fight?")
        if FightChoice == "yes":
            if sword == True:
                print("You fight and defeat Cthulu")
                exit()
            else:
                player_death("getting eaten by Cthulu")
        elif FightChoice == "no":
            encouter()