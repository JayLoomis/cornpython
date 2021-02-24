# command-line application that takes four arguments

    # The name of a text file.
    # A flag indicating whether to encode or decode the text in the file. Use E for encode and D for
    # decode. Don’t worry about any formal “flag” mechanism in the language if you don’t want to--just read the character in. --
    # Accept both upper and lower case letters.
    # A numeric key that represents the number of letters to offset for the cypher.
    # A flag indicating whether to provide output feedback on success.
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description="Caeser Cypher Encryptor and Decryptor")
    parser.add_argument("filename", help="Select your file by name")
    parser.add_argument("mode", choices=['d', 'e'], type=str)
    parser.add_argument("-k", "--keynum", type=int, default=13, help="Key provides a number by which the translation shifts the unicode representation of each character")
    parser.add_argument("-r", "--report", action="store_true")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-D", "--Decrypt", help="Choose D or Decrypt to decipher a text")
    # group.add_argument("-E", "--Encrypt", help="Choose E or Encrypt to encode a text")
    args = parser.parse_args()

    args.mode = args.mode.lower()

    if args.mode == "e":
        report = encrypt(args.filename, args.keynum)
        if args.report:
            print(report)
    elif args.mode == "d":
        report = decrypt(args.filename, args.keynum)
        if args.report:
            print(report)


def encrypt(filename, keynum):
    #create a datestamp
    datestamp = datetime.datetime.now()
    datestamp = datestamp.strftime("%Y%m%d%I%M%S")
    #open user file and start a new file with datestamp
    with open(filename, 'r') as infile, open(filename + "-enc-" + datestamp, 'a') as outfile:
        #read content from first file
        for line in infile:
            #append to new file
            outfile.append(line)

def decrypt(filename, keynum):
    decryptor = open(filename, "w")
    for line in decryptor:
        print(line.strip("\n"))
    decryptor.close()



if __name__ == "__main__": main()