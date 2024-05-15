import requests

class AnagramChecker:
    def __init__(self, word_list_file):
        if word_list_file.startswith("http"):
            response = requests.get(word_list_file)
            if response.status_code == 200:
                word_list_content = response.text
            else:
                raise ValueError("Failed to fetch word list from the provided URL.")
        else:
            with open(word_list_file, 'r') as file:
                word_list_content = file.read()

        self.word_list = set(word.strip().lower() for word in word_list_content.split())

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w) and word.lower() != w:
                anagrams.append(w)
        return anagrams
