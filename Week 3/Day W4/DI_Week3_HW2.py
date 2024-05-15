#Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal("Bengie", 3)
chartreux_cat = Chartreux("Charly", 5)
siamese_cat = Siamese("Simba", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        self_speed = self.run_speed() * self.weight
        other_speed = other_dog.run_speed() * other_dog.weight
        if self_speed > other_speed:
            return f"{self.name} wins the fight!"
        elif self_speed < other_speed:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"
dog1 = Dog("Buddy", 3, 20)
dog2 = Dog("Max", 5, 25)
dog3 = Dog("Charlie", 4, 18)

print(dog1.bark())
print(f"{dog1.name}'s running speed is {dog1.run_speed()} km/h")
print(dog2.bark())
print(f"{dog2.name}'s running speed is {dog2.run_speed()} km/h")
print(dog3.bark())
print(f"{dog3.name}'s running speed is {dog3.run_speed()} km/h")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))

#Dogs Domesticated
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
pet_dog = PetDog("Rocky", 4, 22)
pet_dog.train()
pet_dog.play("Buddy", "Max", "Charlie")
pet_dog.do_a_trick()

#Family
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations! A new member has been born into the family.")
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False
    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
family_instance = Family("Smith", members)
family_instance.born(name='John', age=0, gender='Male', is_child=True)
print("Is Sarah over 18?", family_instance.is_18('Sarah'))
family_instance.family_presentation()

#TheIncredibles Family
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} can use the power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power.")
    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()
incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]
incredibles_instance = TheIncredibles("Incredibles", incredibles_members)
incredibles_instance.incredible_presentation()
incredibles_instance.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackUnknown')
incredibles_instance.incredible_presentation()
