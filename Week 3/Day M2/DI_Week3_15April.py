#Old MacDonald’s Farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_str = ", ".join(animal + ("s" if self.animals[animal] > 1 else "") for animal in animal_types)
        return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_short_info())
print(macdonald.get_info())
