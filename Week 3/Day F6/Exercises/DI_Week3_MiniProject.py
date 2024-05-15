# #Rock, Paper, Scissors
# Below is the game.py file that will be used to execute the Rock_Paper_Scissors.py game.

# import random
# class Game:
#     def get_user_item(self):
#         while True:
#             user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
#             if user_choice in ['rock', 'paper', 'scissors']:
#                 return user_choice
#             else:
#                 print("Invalid choice. Please enter rock, paper, or scissors.")
#     def get_computer_item(self):
#         return random.choice(['rock', 'paper', 'scissors'])
#     def get_game_result(self, user_item, computer_item):
#         if user_item == computer_item:
#             return 'draw'
#         elif (user_item == 'rock' and computer_item == 'scissors') or \
#              (user_item == 'paper' and computer_item == 'rock') or \
#              (user_item == 'scissors' and computer_item == 'paper'):
#             return 'win'
#         else:
#             return 'loss'
#     def play(self):
#         user_item = self.get_user_item()
#         computer_item = self.get_computer_item()
#         result = self.get_game_result(user_item, computer_item)
#         print(f"You selected {user_item}. The computer selected {computer_item}. You {result}.")
#         return result

#Below is the Rock_Paper_Scissors.py
from game import Game
def get_user_menu_choice():
    print("Menu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice
def print_results(results):
    print("Game Results:")
    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")
    print("Thank you for playing!")
def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break
        else:
            print("Invalid choice. Please choose again.")
main()


#Mini Project : Vaccines
class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age >= 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for i, p in enumerate(self.humans):
            if p == person:
                return i
        return -1

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                return self.humans.pop(i)
        return None

    def sort_by_age(self):
        self.humans.sort(key=lambda x: (not x.priority, x.age))

    def rearrange_queue(self):
        rearranged_queue = []
        for person in self.humans:
            if not rearranged_queue or person.family != rearranged_queue[-1].family:
                rearranged_queue.append(person)
        self.humans = rearranged_queue

# Creating Human instances
alice = Human("1", "Alice", 65, True, "A")
bob = Human("2", "Bob", 30, False, "O")
carol = Human("3", "Carol", 70, True, "AB")
dave = Human("4", "Dave", 40, False, "B")
eve = Human("5", "Eve", 55, True, "A")

# Adding family members
alice.add_family_member(bob)
alice.add_family_member(carol)
bob.add_family_member(alice)
dave.add_family_member(eve)

# Creating Queue instance
vaccine_queue = Queue()

# Adding humans to the queue
vaccine_queue.add_person(alice)
vaccine_queue.add_person(bob)
vaccine_queue.add_person(carol)
vaccine_queue.add_person(dave)
vaccine_queue.add_person(eve)

# Sorting the queue by age
vaccine_queue.sort_by_age()

# Getting the next person in the queue
next_person = vaccine_queue.get_next()
print("Next person in the queue:", next_person.name if next_person else "None")

# Getting the next person with blood type "A"
next_person_A = vaccine_queue.get_next_blood_type("A")
print("Next person with blood type A:", next_person_A.name if next_person_A else "None")

# Rearranging the queue to avoid family members standing next to each other
vaccine_queue.rearrange_queue()

# Printing the queue
print("Queue after rearrangement:")
for person in vaccine_queue.humans:
    print(person.name)

# Swapping positions of two people in the queue
vaccine_queue.swap(carol, eve)

# Getting the next person in the queue after swapping
next_person_after_swap = vaccine_queue.get_next()
print("Next person in the queue after swap:", next_person_after_swap.name if next_person_after_swap else "None")
