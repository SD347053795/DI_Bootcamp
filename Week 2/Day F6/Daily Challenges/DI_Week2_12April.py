#Challenge 1 : Sorting
def sort_words(input_str):
    words = input_str.split(',')
    sorted_words = sorted(words)
    sorted_str = ','.join(sorted_words)
    return sorted_str

input_str = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_str)
print("Sorted sequence:", sorted_sequence)

#Challenge 2 : Longest Word
import re
def longest_word(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    longest = max(words, key=len)
    return longest
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
