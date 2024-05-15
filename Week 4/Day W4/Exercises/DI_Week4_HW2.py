#Exercise 1
import requests
import random
def get_words_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            words = response.text.splitlines()
            return words
        else:
            print("Failed to retrieve words from URL:", response.status_code)
            return []
    except Exception as e:
        print("Failed to retrieve words from URL:", e)
        return []
def get_random_sentence(length, words):
    random_words = [random.choice(words) for _ in range(length)]
    random_sentence = ' '.join(random_words).lower()
    return random_sentence
def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence based on the words from the SOWPODS list.")
    url = "https://norvig.com/ngrams/sowpods.txt"
    words = get_words_from_url(url)
    if not words:
        print("Exiting program.")
        return
    while True:
        try:
            length = int(input("How long do you want the sentence to be (between 2 and 20)? "))
            if length < 2 or length > 20:
                raise ValueError("Length must be between 2 and 20.")
            break
        except ValueError:
            print("Please enter a valid integer between 2 and 20.")
    random_sentence = get_random_sentence(length, words)
    print("Random Sentence:", random_sentence)
    main()

Exercise 2
import json
sample_dict = json.loads(samplejson)
salary = sample_dict["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)
sample_dict["company"]["employee"]["birth_date"] = "1990-01-01"
with open("updated_json_file.json", "w") as json_file:
    json.dump(sample_dict, json_file, indent=4)
print("Updated JSON file saved successfully.")
