def print_hello(a,b):
    print(a+b)
print_hello(int(input("give me a number")),int(input("and now another number")))



def multiplier(a_list):
    b_list=[]
    for i in a_list:
        b_list.append(i * 2)
    return (b_list)

list_input=[1,2,3,4,5,6,7,8,9]
print(multiplier(list_input))
print(multiplier(multiplier(list_input)))


a=4

def update_local_var():

    a = 17
    print("the value of the var inside is:", a)

update_local_var()
print("the value of the var outside is:", a)




a=4

def update_global_var():
    global a
    a = 17
    print("the value of the var inside is:", a)

update_global_var()
print("the value of the var outside is:", a)