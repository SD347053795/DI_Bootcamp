from anagram_checker import AnagramChecker

def get_user_input():
    return input("Enter a word (or 'exit' to quit): ").strip()

def validate_input(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    return True

def display_anagrams(word, anagrams):
    print(f"\nYOUR WORD: \"{word}\"")
    if anagrams:
        print("This is a valid English word.")
        print("Anagrams for your word:", ", ".join(anagrams))
    else:
        print("Sorry, no anagrams found for your word.")

def main():
    anagram_checker = AnagramChecker("https://norvig.com/ngrams/sowpods.txt")

    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            break

        if validate_input(user_input):
            word = user_input.lower()
            if anagram_checker.is_valid_word(word):
                anagrams = anagram_checker.get_anagrams(word)
                display_anagrams(word, anagrams)
            else:
                print("Sorry, this is not a valid English word.")

if __name__ == "__main__":
    main()
