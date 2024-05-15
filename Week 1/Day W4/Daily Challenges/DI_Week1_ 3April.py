#Challenge 1
#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
def generate_multiples(number, length):
    multiples = []
    for i in range(1, length + 1):
        multiples.append(number * i)
    return multiples
def main():
    try:
        number = int(input("Enter a number: "))
        length = int(input("Enter the desired length of the list: "))
        if number <= 0 or length <= 0:
            print("Please enter positive numbers.")
            return
        result = generate_multiples(number, length)
        print(f"List of multiples of {number} until length {length}:")
        print(result)
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()


#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
def remove_duplicates(input_string):
    # Initialize an empty string to store the result
    result = ""
    for i in range(len(input_string)):
        # If the current character is not the same as the next one, append it to the result
        if i == len(input_string) - 1 or input_string[i] != input_string[i + 1]:
            result += input_string[i]
    return result
user_input = input("Enter a string: ")
print("String with consecutive duplicates removed:", remove_duplicates(user_input))
