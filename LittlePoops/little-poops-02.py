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
        self.dictionary = self.dict_file.readlines()
        

    @staticmethod
    def is_anagram(word,anagram):
        word = lower(word)
        wordsorted = sorted(word)
        wordsorted = "".join(wordsorted)
        anagram = lower(anagram)
        anagramsorted = sorted(anagram)
        anagramsorted = "".join(anagramsorted)

        if wordsorted == anagramsorted:
            return True
        else:
            return False

    def find_anagram(self, word):

        for entry in self.dictionary:


    def list_anagrams(self, word):
        results = []
        for entry in self.dictionary:
            # check = entry.rstrip()
            if is_anagram(entry, word):
                results.append(entry)
            else:
                continue
        if results == []:
            return word
        else:
            return results


class Interface:

    #def __init__(self):
        #self.dict_file = dictionary.txt

    def start(self):
        self.source_dict = "dictionary.txt"
        anagrams = Anagrammer(self.source_dict)

        print("enter a word:\n")
        word = input()
        anagrams.list_anagrams(word)





def main():
    ui = Interface()
    ui.start()

if __name__ == "__main__" : main()