#Exercise 1 : Set
my_fav_numbers = {2, 3, 5, 7, 11, 13, 17}
my_fav_numbers.update({19, 23})
my_fav_numbers.remove(23)
friend_fav_numbers = {9, 18, 27, 36, 45, 54, 63}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Our Favorite Numbers:", our_fav_numbers)

#Exercise 2: Tuple
my_tuple = (1,2,3,4,5)
print('my_tuple: is now set and it is not possible to add another integer in this tuple')

#Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket[3] = 'Kiwi'
basket[0] = 'Apples'
apple_count = basket.count("Apples")
basket.clear()
print(basket)

#OR
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# apple_count = basket.count("Apples")
# basket.clear()
# print(basket)

#Exercise 4: Floats
#Floats are used to represent not whole numbers or partial numbers, such as 3.14 or -0.01.
floating = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(floating)

#or
# sequence = []
# for i in range (1,6):
#     decimal =  i + 0.5
#     sequence.append(i)
#     sequence.append(decimal)
# print(sequence[1:-1])

#Exercise 5: For Loop
for i in range(1, 21):
    print(i)

for j in range(1, 21):
    if j % 2 == 0:
        print(j)


#Exercise 6 : While Loop
my_name = "Shmuel Drucker"

while True:
    user_name = input("Please enter your name: ")
    if user_name == my_name:
        print("Thank you for entering your name!")
        break
    else:
        print("That's not my name. Please try again.")


#Exercise 7: Favorite Fruits
favorite_fruits = input("Please enter your favorite fruit(s), separated by a single space: ")
favorite_fruits_list = favorite_fruits.split('apple, mango, cherry, kiwi, watermelon, blueberry, orange, pear')
print("Your favorite fruits are:", favorite_fruits_list)
chosen_fruit = input("Now, please enter the name of any fruit: ")
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")



#Exercise 8: Who Ordered A Pizza?
toppings = []
total_price = 10
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ").lower()
    if topping == 'quit':
        break
    else:
        print("Adding", topping, "to your pizza.")
        toppings.append(topping)
        total_price += 2.5
print("\nYour pizza includes the following toppings:")
for topping in toppings:
    print("- " + topping)
print("\nTotal price for your pizza is: $", total_price)


#Exercise 9: Cinemax
adult_price = 15
child_price = 10
baby_price = 0
adult = int(input('How many people of 12: '))
children = int(input('How many children under 12: '))
total_adult_cost = adult * adult_price
total_child_cost = children * child_price
total_cost = total_adult_cost + total_child_cost
print("Total cost for adults: $", total_adult_cost)
print("Total cost for children: $", total_child_cost)
print("Total cost: $", total_cost)

teen_list = ['teen1', 'teen2', 'teen3']
permitted_teens = []
for teen in teen_list:
    age= int(input(f"what is {teen}'s age"))
    if age in range(16, 21):
        permitted_teens.append(teen)
    else:
        print(f'{teen} is too young to enter this movie')
print(f'{permitted_teens} are allowed to enter')

#Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"Your {sandwich} is ready.")
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

