#Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Currency' and {}".format(type(other)))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        else:
            raise TypeError("Unsupported operand type(s) for +=: 'Currency' and {}".format(type(other)))

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)  # Output: 20 dollars
try:
    print(c1 + c3)
except TypeError as e:
    print(e)

# #Exercise 2
# #func.py
# def add_numbers(num1, num2):
#     result = num1 + num2
#     print("The result of adding", num1, "and", num2, "is:", result)
#
# #exercise_one.py
# from func import add_numbers
# add_numbers(5, 7)

#Exercise 3
import string
import random
def generate_random_string(length):
    letters = string.ascii_letters  # contains both upper and lower case letters
    return ''.join(random.choice(letters) for _ in range(length))
random_string = generate_random_string(5)
print(random_string)

#Exercise 4
import datetime
def display_current_date():
    current_date = datetime.datetime.now().date()
    print("Current date:", current_date)
display_current_date()

#Exercise 5
from datetime import datetime
def time_until_january_1st():
    current_date = datetime.now()
    january_1st_next_year = datetime(current_date.year + 1, 1, 1)
    time_difference = january_1st_next_year - current_date
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")
time_until_january_1st()

#Exercise 6
from datetime import datetime
def minutes_lived(birthdate):
    # Convert birthdate string to datetime object
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    current_date = datetime.now()
    time_difference = current_date - birthdate
    minutes = int(time_difference.total_seconds() / 60)
    print(f"You have lived for approximately {minutes} minutes.")
birthdate = "1990-05-15"
minutes_lived(birthdate)

# #Exercise 7
# from faker import Faker
# fake = Faker()
# users = []
# def add_user():
#     user = {
#         'name': fake.name(),
#         'address': fake.address(),
#         'language_code': fake.language_code()
#     }
#     users.append(user)
# for _ in range(5):
#     add_user()
# print(users)
