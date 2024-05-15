#Exercise 1 : What Are You Learning?
def display_message():
    print("So far in this course I am learning the foundations of Python.")
display_message()

#Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print("One of my favorite books is:", title)
favorite_book("bilvavi mishkan evneh")

# Exercise 3 : Some Geography
def describe_city(city, country="Unknown"):
    print(city, "is in", country)
describe_city("Jerusalem")
describe_city("Jerusalem", "Israel")

#Exercise 4 : Random
import random
def compare_numbers(guess):
    random_number = random.randint(1, 100)
    print("Generated number:", random_number)
    if guess == random_number:
        print("Success! You guessed the right number.")
    else:
        print("Fail! The numbers are different.")
        print("Your guess:", guess)
guess = int(input("Enter a number between 1 and 100: "))
compare_numbers(guess)

#Exercise 5 : Let’s Create Some Personalized Shirts!
def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is", size, "and the text is", text)
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Python is awesome!")
make_shirt(text="Code On", size="extra large")


#Exercise 6 : Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magicians):
    for magician in sorted(magicians):
        print(magician)
def make_great(magicians):
    for maker in range(len(magicians)):
        magicians[maker] += " the Great"
make_great(magician_names)
show_magicians(magician_names)


