print("Hello Python")
print(9/2)
print(9//2)
print(9%2)
print(9**2)
print(2**9)

first_value=14
first_value += first_value*0.12
print("the final price is:", first_value)

second_value = 20
second_value -= second_value*0.40
print("the final price with discount is:", second_value)

name = input("what is your name? ")
surname = input("what is your surname? ")
age = int(input("what is your age? "))
height = float(input("what is your height in meters? "))

print("your name is %s %s, you are %d years old and %.2f m tall" % (name,surname,age,height))

big_number = int(input("pick a big number: "))
if big_number <= 100:
    print("That's a small number")
elif big_number <= 1000:
    print("that's not a big number yet")
else:
    print("That's an adequately huge number!")

if int(input("pick a number: ")) % 2 == 0:
    print("thats a even number")
else:
    print("thats a odd number")
