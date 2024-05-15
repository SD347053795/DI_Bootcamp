#Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cats = [
    Cat("Whiskers", 5),
    Cat("Mittens", 8),
    Cat("Fluffy", 3)
]

oldest_cat = max(cats, key=lambda cat: cat.age)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Rex", 50)
print("David's dog details:")
print("Name:", davids_dog.name)
print("Height:", davids_dog.height, "cm")
davids_dog.bark()
davids_dog.jump()
print()

sarahs_dog = Dog("Teacup", 20)
print("Sarah's dog details:")
print("Name:", sarahs_dog.name)
print("Height:", sarahs_dog.height, "cm")
sarahs_dog.bark()
sarahs_dog.jump()
print()

if davids_dog.height > sarahs_dog.height:
    print("The bigger dog is:", davids_dog.name)
elif sarahs_dog.height > davids_dog.height:
    print("The bigger dog is:", sarahs_dog.name)
else:
    print("Both dogs are of the same height.")

#Who’s The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Afternoon At The Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been successfully added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        return sorted_animals
    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Groups of animals in the zoo:")
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")
ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Tiger")
ramat_gan_safari.get_animals()

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Gorilla")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()
