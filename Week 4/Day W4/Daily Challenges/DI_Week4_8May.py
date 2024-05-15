#Make sure to have the the_stranger.txt file in the same directory as your Python script or provide the correct path to the file.

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_list = self.text.split()
        return word_list.count(word)

    def most_common_word(self):
        word_list = self.text.split()
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return max(word_count, key=word_count.get)

    def unique_words(self):
        word_list = self.text.split()
        return list(set(word_list))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

simple_text = "A good book would sometimes cost as much as a good house."
text_instance = Text(simple_text)

print("Frequency of 'good':", text_instance.word_frequency("good"))
print("Most common word:", text_instance.most_common_word())
print("Unique words:", text_instance.unique_words())

file_text_instance = Text.from_file('the_stranger.txt')

print("\nFrequency of 'the':", file_text_instance.word_frequency("the"))
print("Most common word:", file_text_instance.most_common_word())
print("Unique words:", file_text_instance.unique_words())
