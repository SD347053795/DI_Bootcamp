#XP
#Exercise 1 : Hello World
print('Hello World\n'*4)

#Exercise 2 : Some Math
result = (99**3) * 8
print(result)

#Exercise 3 : What Is The Output?
a = bool(5 < 3)
print(f"5 < 3 is {a}")
b = bool(3 == 3)
print(f"3 == 3 is {b}")
c = bool(3 == "3")
print(f"3 == '3'is {c}")
print("'3' > 3 is a TypeError")
d = bool("Hello" == "hello")
print(f"'Hello' == 'hello' is {d}")

#Exercise 4 : Your Computer Brand
computer_brand = 'ThinkPad'
print(f"I have a {computer_brand} computer.")

#Exercise 5 : Your Information
name = "Shmuel Drucker"
age = 31
shoe_size = 44
info = f"{name} lived in Colorado. {name}'s favorite shoe store was in Boulder, Colorado and {name}'s shoe size is {shoe_size}. Now {name} is learning how to code at {age} years old."
print(info)

# Exercise 6 : A & B
a = 19
b = 7
if a>b:
    print('Hello World')

#Exercise 7 : Odd Or Eve
my_name = 'Shmuel Drucker'
user_name = input('What is your name? ')
if user_name.lower() == my_name.lower():
    print("Wow, we have the same name! What are the odds?")
else:
    print(f"Nice to meet you, {user_name}! Would you like to discover an interesting fact about your name together?")

#Exercise 9 : Tall Enough To Ride A Roller Coaster
height_CM = float(input('Please tell me your hight in CM'))
if (height_CM > 145):
    print("You are tall enough to ride!")
else:
    print("Sorry, you need to grow some more to ride.")




#XP Gold
print('Hello World\n'*4 + 'I Love Python\n'*4)

month = int(input('Please give me a Month (1-12): '))
if month in[3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")