#Tic Tac Toe
tic_tac_toe = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def display_board():
    board = f'''
    TIC TAC TOE
    *****************
    *   {tic_tac_toe[0][0]} | {tic_tac_toe[0][1]} | {tic_tac_toe[0][2]}   *
    *  ---|---|---  *
    *   {tic_tac_toe[1][0]} | {tic_tac_toe[1][1]} | {tic_tac_toe[1][2]}   *
    *  ---|---|---  *
    *   {tic_tac_toe[2][0]} | {tic_tac_toe[2][1]} | {tic_tac_toe[2][2]}   *
    *****************
    '''
    print(board)
def player_input(player):
    while True:
        position = input("Player {} - Enter your move (row, column) separated by comma: ".format(player))
        try:
            row, col = map(int, position.split(','))
            if 1 <= row <= 3 and 1 <= col <= 3 and tic_tac_toe[row - 1][col - 1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid entry! Please try again.")
        except ValueError:
            print("Invalid entry! Please enter two integers separated by a comma.")
def check_win():
    for row in tic_tac_toe:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if tic_tac_toe[0][col] == tic_tac_toe[1][col] == tic_tac_toe[2][col] != ' ':
            return tic_tac_toe[0][col]
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] != ' ':
        return tic_tac_toe[0][0]
    if tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] != ' ':
        return tic_tac_toe[0][2]
    if all([cell != ' ' for row in tic_tac_toe for cell in row]):
        return "tie"
    return False
def play():
    current_player = 'X'
    while True:
        display_board()
        row, col = player_input(current_player)
        if 0 <= row < 3 and 0 <= col < 3 and tic_tac_toe[row][col] == ' ':
            tic_tac_toe[row][col] = current_player
            winner = check_win()
            if winner:
                display_board()
                if winner == "tie":
                    print("It's a tie!")
                else:
                    print("Player {} wins!".format(winner))
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move! Please try again.")

play()

#Hangman
import random
def choose_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
                 'credit card', 'rush', 'south']
    return random.choice(wordslist)
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '*'
    return display
def display_hangman(attempts):
    stages = [
        '''
         _____
         |   |
         |   0
         |  /|\
         |  / \
         _______
        ''',
        '''
         _____
         |   |
         |   0
         |  /|\
         |  /
         _______
        ''',
        '''
         _____
         |   |
         |   0
         |  /|\
         |
         _______
        ''',
        '''
         _____
         |   |
         |   0
         |  /|
         |
         _______
        ''',
        '''
         _____
         |   |
         |   0
         |   |
         |
         _______
        ''',
        '''
         _____
         |   |
         |   0
         |
         |
         _______
        ''',
        '''
         _____
         |   |
         |
         |
         |
         _______
         '''
    ]
    print(stages[min(attempts, len(stages) - 1)])
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(display_hangman(attempts))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
            display_hangman(attempts)
            print("Attempts Left:", attempts)
        print("Word:", display_word(word, guessed_letters))
    if attempts ==0:
        print("You've run out of attempts. The word was:", word)
hangman()

#Challenge 1
my_list = [1, 2, 3, 4, 5]
item_to_insert = 6
index_to_insert_at = 5
my_list.insert(index_to_insert_at, item_to_insert)
print("Modified List:", my_list)

#Challenge 2
input_string = "I'm a Jew and I'm proud and I'm singing out loud HaShem is always watching over us."
spaces_count = input_string.count(' ')
print("Number of spaces:", spaces_count)

#Challenge 3
input_string = "I'm a Jew and I'm proud and I'm singing out loud HaShem is always watching over us."
upper_count = sum(1 for char in input_string if char.isupper())
lower_count = sum(1 for char in input_string if char.islower())
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

#Challenge 4
def my_sum(arr):
    return sum(arr)
print(my_sum([1, 5, 4, 2]))

#Challenge 5
def find_max(lst):
    return max(lst)
print(find_max([0, 1, 3, 50]))

#Challenge 6
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(4))

#Challenge 7
def list_count(lst, element):
    return sum(1 for item in lst if item == element)
print(list_count(['a', 'a', 't', 'o'], 'a'))

#Challenge 8
import math
def norm(lst):
    return math.sqrt(sum(x ** 2 for x in lst))
print(norm([1, 2, 2]))

#Challenge 9
def is_mono(arr):
    return bool(all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))) or bool(all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))
print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))

#Challenge 10
def longest_word(words):
    print("Longest word:", max(words, key=len))
words_list = ["Rosh Chodesh", "Shabbat", "Pesach", "Rosh Hashannah", "Yom Kippur", "Sukkot", "Channukah", "Purim", "Shavuot"]
longest_word(words_list)

#Challenge 11
def separate_integers_and_strings(lst):
    integers = [x for x in lst if isinstance(x, int)]
    strings = [x for x in lst if isinstance(x, str)]
    return integers, strings
mixed_list = [1, 'passover', 3, 'matzah', 5, 'seder']
integers, strings = separate_integers_and_strings(mixed_list)
print("Integers:", integers)
print("Strings:", strings)

#Challenge 12
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome('radar'))
print(is_palindrome('John'))

#Challenge 13
def sum_over_k(sentence, q):
    return sum(1 for word in sentence.split() if len(word) > q)
sentence = 'Do or do not there is no try'
q = 2
print(sum_over_k(sentence, q))

#Challenge 14
def dict_avg(dictionary):
    return sum(dictionary.values()) / len(dictionary)
print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))  # Output: 3.0

#Challenge 15
def common_div(a, b):
    return list(set(range(1, a + 1)) & set(range(1, b + 1)))
print(common_div(10, 20))  # Output: [1, 2, 5, 10]

#Challenge 16
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
print(is_prime(11))

#Challenge 17
def weird_print(lst):
    print([num for index, num in enumerate(lst) if index % 2 == num % 2 == 0])
weird_print([1, 2, 2, 3, 4, 5])

#Challenge 18
def type_count(**kwargs):
    return {type_name: sum(1 for value in kwargs.values() if type(value).__name__ == type_name) for type_name in set(type(value).__name__ for value in kwargs.values())}
print(type_count(a=1, b='string', c=1.0, d=True, e=False))


#Challenge 19
def my_split(string, delimiter=None):
    return string.split(delimiter) if delimiter else string.split()
print(my_split("Hello world"))  # Output: ['Hello', 'world']
print(my_split("apple,banana,cherry", ","))

#Challenge 20
def to_password_format(input_string):
    return '*' * len(input_string)
input_string = "mypassword"
print(to_password_format(input_string))

#Challenge 22
rows = 3
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1) + " " * (rows - i))
print()
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
print()
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * i)

#Challenge 23
my_list = [2, 24, 12, 354, 233] # Define a list of integers
for i in range(len(my_list) - 1):  # Loop over the indices of the list except for the last one
    minimum = i # Set the current index as the minimum
    for j in range(i + 1, len(my_list)):  # Loop over the indices from the next index to the end of the list
        if my_list[j] < my_list[minimum]:   # Compare the element at index j with the minimum element found so far
            minimum = j # If the element at index j is smaller, update the minimum index
            if minimum != i:   # Check if minimum index is not equal to current index
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]   # Swap the elements at indices i and minimum
print(my_list)  # Print the sorted list