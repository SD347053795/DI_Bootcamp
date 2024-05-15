# Quizz
# A class is a blueprint for creating objects in object-oriented programming.
# An instance is a specific realization of a class.
# Encapsulation is bundling the data and methods that operate on the data into a single unit, often a class.
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.
# Inheritance is a mechanism in object-oriented programming where a new class inherits properties and behaviors from an existing class.
# Multiple inheritance is the ability of a class to inherit properties and behavior from more than one parent class.
# Polymorphism is the ability of different classes to be treated as instances of a common superclass.
# Method Resolution Order (MRO) defines the order in which methods are resolved in the presence of inheritance in multiple inheritance scenarios.

#Create A Deck Of Cards Class
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
class Deck:
    def __init__(self):
        self.cards = []
        self.populate_deck()
    def populate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
deck = Deck()
deck.shuffle()
print("Shuffled deck:")
for card in deck.cards:
    print(card.suit, card.value)
print("\nDealing one card:")
dealt_card = deck.deal()
print("Dealt card:", dealt_card.suit, dealt_card.value)
print("\nRemaining cards in the deck:")
for card in deck.cards:
    print(card.suit, card.value)


#Air Management System
from datetime import datetime

class Airline:
    def __init__(self, airline_id, name):
        self.id = airline_id
        self.name = name
        self.planes = []

class Airplane:
    def __init__(self, plane_id, company):
        self.id = plane_id
        self.current_location = None
        self.company = company
        self.next_flights = []
    def fly(self, destination):
        if self.available_on_date(datetime.now().date(), self.current_location):
            self.current_location.scheduled_departures.remove(self.next_flights[0])
            self.next_flights.pop(0)
            self.current_location = destination
            destination.scheduled_arrivals.append(self.next_flights[0])
            print(f"Flight {self.next_flights[0].id} has taken off and is en route to {destination.city}")
        else:
            print("The airplane is not available for flight at this time.")
    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date == date:
                return flight.destination
        return self.current_location
    def available_on_date(self, date, location):
        if self.current_location != location:
            return False
        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True

class Flight:
    def __init__(self, flight_id, date, origin, destination, plane):
        self.id = flight_id
        self.date = date
        self.origin = origin
        self.destination = destination
        self.plane = plane
    def take_off(self):
        self.plane.fly(self.destination)
    def land(self):
        self.plane.current_location = self.destination

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []
    def schedule_flight(self, destination, date):
        for plane in self.planes:
            if plane.available_on_date(date, self):
                flight_id = f"{destination.city}-{plane.company.id}-{date}"
                new_flight = Flight(flight_id, date, self, destination, plane)
                self.scheduled_departures.append(new_flight)
                destination.scheduled_arrivals.append(new_flight)
                plane.next_flights.append(new_flight)
                print(f"Flight {flight_id} scheduled from {self.city} to {destination.city} on {date}")
                return
        print("No available airplane for this flight.")
    def info(self, start_date, end_date):
        print(f"Scheduled flights from {self.city} between {start_date} and {end_date}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id} to {flight.destination.city} on {flight.date}")

# Example usage
if __name__ == "__main__":
    airline = Airline("AA", "American Airlines")
    airport_nyc = Airport("NYC")
    airport_lax = Airport("LAX")
    airplane = Airplane(1, airline)
    airplane.current_location = airport_nyc
    airline.planes.append(airplane)
    airport_nyc.planes.append(airplane)
    # Schedule a flight
    airport_nyc.schedule_flight(airport_lax, datetime(2024, 4, 20))
    # Display scheduled flights
    airport_nyc.info(datetime(2024, 4, 18), datetime(2024, 4, 22))
    # Take off
    airport_nyc.scheduled_departures[0].take_off()
    # Land
    airport_lax.scheduled_arrivals[0].land()