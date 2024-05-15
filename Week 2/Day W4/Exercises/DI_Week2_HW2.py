# #Exercise 1 : Temperature Advice
# import random
# def get_random_temp():
#     return random.randint(-10, 40)
# print(get_random_temp())
# def main():
#     temperature = get_random_temp()
#     print("The temperature right now is {} degrees Celsius.".format(temperature))
#     if temperature < 0:
#             print("Stay inside it is too cold today.")
#     elif 0 <= temperature < 16:
#             print("Best bundle up.")
#     elif 16 <= temperature < 24:
#             print("Lookin good out there, time to start the summer tan")
#     elif 24 <= temperature < 32:
#             print("Suns out Guns out...Don't forget the sunscreen.")
#     else:
#             print("Way to hot outside stay in with the AC blastin.")
# main()
import random
def get_random_temp(month):
    if month in [12, 1, 2]:
        return round(random.uniform(-10, 16), 1)
    elif month in [3, 4, 5]:
        return round(random.uniform(0, 23), 1)
    elif month in [6, 7, 8]:
        return round(random.uniform(16, 40), 1)
    elif month in [9, 10, 11]:
        return round(random.uniform(0, 23), 1)
    else:
        raise ValueError("Invalid month. Please enter a number between 1 and 12.")
def main():
    month = int(input("Please enter the number of the month (1 = January, 12 = December): "))
    temperature = get_random_temp(month)
    print("The temperature right now is {} degrees Celsius.".format(temperature))
    if temperature < 0:
        print("Stay inside it is too cold today.")
    elif 0 <= temperature < 16:
        print("Best bundle up.")
    elif 16 <= temperature < 24:
        print("Lookin good out there, time to start the summer tan.")
    elif 24 <= temperature < 32:
        print("Suns out Guns out...Don't forget the sunscreen.")
    else:
        print("Way to hot outside stay in with the AC blastin.")
main()

#Exercise 2 : Star Wars Quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def take_quiz(questions):
    correct_answers = 0
    wrong_answers = []

    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            correct_answers += 1
        else:
            wrong_answers.append(question["question"])

    return correct_answers, wrong_answers
def inform_user(correct_answers, wrong_answers):
    print("Quiz Results:")
    print("Correct Answers: {}".format(correct_answers))
    print("Incorrect Answers: {}".format(len(wrong_answers)))
    if len(wrong_answers) > 0:
        print("The following questions were answered incorrectly:")
        for question in wrong_answers:
            print("- " + question)
def main():
    print("Welcome to the Star Wars Quiz!")
    correct_answers, wrong_answers = take_quiz(data)
    inform_user(correct_answers, wrong_answers)
main()

#Exercise 3 : When Will I Retire ?
import datetime


def get_age(date_of_birth):
    current_date = datetime.date.today()
    birth_date = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = current_date.year - birth_date.year - (
                (current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age


def can_retire(gender, date_of_birth):
    current_year = datetime.date.today().year
    retirement_age_men = 67
    retirement_age_women = 62

    dob_year, dob_month, dob_day = map(int, date_of_birth.split('-'))

    age = get_age(date_of_birth)

    if gender.lower() == 'male':
        retirement_age = retirement_age_men
    elif gender.lower() == 'female':
        retirement_age = retirement_age_women
    else:
        raise ValueError("Gender should be 'male' or 'female'")

    if gender.lower() == 'female' and dob_year > 1947:
        retirement_age = retirement_age_women

    return age >= retirement_age

gender = input("Enter your gender (male/female): ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

if can_retire(gender, date_of_birth):
    print("You can retire.")
else:
    print("You cannot retire yet.")


#Exercise 4:
def calculate_sequence(X):
    total = 0
    for i in range(1, 5):
        num_str = str(X) * i
        total += int(num_str)
    return total
def main():
    X = int(input("Enter a number: "))
    result = calculate_sequence(X)
    print("The result is:", result)
main()
