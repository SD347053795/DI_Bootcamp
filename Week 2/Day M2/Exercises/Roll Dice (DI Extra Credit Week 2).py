# # Exercise 1 : Double Dice
# # Instructions
# #   1. Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# #   2. Create a function called throw_until_doubles.
# #       2A. It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# #           For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# #       2B. This function should return the number of times it threw the dice in total. In the example above, it should return 3.
# #   3. Create a main function.
# #       It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
# #   4. After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# #   5. Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# #   6. For example:
# #       6A. If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# #           (1, 2), (3, 1), (5, 5)
# #           (3, 3)
# #           (2, 4), (1, 2), (3, 4), (2, 2)
# #
# #       6B. Then my output would show something like this:
# #           Total throws: 8
# #           Average throws to reach doubles: 2.67.

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        throws += 1
        roll1 = throw_dice()
        roll2 = throw_dice()
        if roll1 == roll2:
            return throws

def main():
    double_time = []
    total_throws = 0
    for throws in range(100):
        throws_to_doubles = throw_until_doubles()
        double_time.append(throws_to_doubles)
        total_throws += throws_to_doubles

    print(f"Total throws to reach 100 doubles: {total_throws}")
    average_throws = total_throws / 100
    print(f"Average throws to reach doubles: {average_throws:.2f}")
    return double_time

if __name__ == "__main__":
    results = main()
    print("Results:", results)
