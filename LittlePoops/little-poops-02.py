# Let's turn this poop into a little OOP!

# Build a class named Anagrammer:

#     Create a constructor that takes one positional argument named dict_file,
#         In the constructor, define an instance variable named dictionary.
#             Open the file whose name was passed as dict_file and read its contents into the dictionary list
#     Create a static method named is_anagram:
#         Use the function requirements from the original issue post above for this method.
#     Create an instance method named find_anagram that takes one parameter: word:
#         word is the word for which to find an anagram
#         Shuffle the dictionary list (there's a library function that does this, it's with the other random stuff)
#         Find the first anagram in the shuffled dictionary and return it, searching for single-word anagrams only.
#         If there is no anagram, return the original word
#     Create an instance method named list_anagrams that takes one parameter: word:
#         word is the word for which to list the anagrams
#         Sort the word dictionary
#         Find all of the possible anagrams for word, searching for single-word anagrams only
#         Return a sorted list of all the anagrams you found, or a list containing only the original word if there are none

# Build a simple UI that surfaces all of the functionality of the Anagrammer class to the user. You decide whether you want to make a single-instance class to do the UI work, or to do it procedural style. In either case, you'll make a single instance of Anagrammer to use.

# Considerations

#     Don't waste time trying to finding the perfect, most clever solution to finding anagrams! Get something that works, then
#     improve it as you have time and inclination.
#     Think about why we're using an object for Anagrammer, since we'll only be using a single instance of it. There's at least one
#     good reason.
#     Think about what it would take to:
#         Find multi-word anagrams
#         Filter the dictionary list to quickly get to a list that's worth the effort of a deeper comparison

import random
import sys

class Anagrammer:

    def __init__(self, dict_file):
        self.dict_file = open(dict_file)
        self.dictionary = self.dict_file.read().splitlines()
        # print(self.dictionary[0])
        

    @staticmethod
    def is_anagram(word,anagram):
        word = word.lower()
        wordsorted = sorted(word)
        wordsorted = "".join(wordsorted)
        anagram = anagram.lower()
        anagramsorted = sorted(anagram)
        anagramsorted = "".join(anagramsorted)

        if wordsorted == anagramsorted:
            return True
        elif wordsorted != anagramsorted:
            return False

    def find_anagram(self, word):
        result = ""
        shuf_dict = random.sample(self.dictionary, len(self.dictionary))
        # print(self.dictionary[0:5])
        # print(len(shuf_dict))
        # print(shuf_dict[0:5])
        for entry in shuf_dict:
            if Anagrammer.is_anagram(word, entry) == True:
                result = entry
                return result
            else:
                answer = "There are no anagrams of {}".format(word)
                return answer

    def list_anagrams(self, word):
        results = []
        for entry in self.dictionary:
            # check = entry.rstrip()
            if Anagrammer.is_anagram(word, entry) == True:
                results.append(entry)
        if results == []:
            answer = "There are no anagrams of {}".format(word)
            return answer
        else:
            return results


class Interface:

    def start(self):
        # pick the source dictionary
        self.source_dict = "dictionary.txt"
        # intantiate Anagrammer
        anagrams = Anagrammer(self.source_dict)

        print("enter a word:\n")
        word = input()
        print("1 or *?")
        m = input()
        if m == "1":
            answer = anagrams.find_anagram(word)
            print(answer)
        elif m == "*":
            answer = anagrams.list_anagrams(word)
            print(answer)




def main():
    ui = Interface()
    ui.start()

if __name__ == "__main__" : main()