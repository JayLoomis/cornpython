# command-line application that takes four arguments

    # The name of a text file.
    # A flag indicating whether to encode or decode the text in the file. Use E for encode and D for
    # decode. Don’t worry about any formal “flag” mechanism in the language if you don’t want to--just read the character in. --
    # Accept both upper and lower case letters.
    # A numeric key that represents the number of letters to offset for the cypher.
    # A flag indicating whether to provide output feedback on success.
import argparse

parser = argparse.ArgumentParser(description="Caeser Cypher key")
parser.add_argument("filename", help="Select your file by name")
parser.add_argument("-k", "--Keycode", type=int, required=True, help="Select the keycode (numeral) to shift the cypher")

if __name__ == "__main__": main()