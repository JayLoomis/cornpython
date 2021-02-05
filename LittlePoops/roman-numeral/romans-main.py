import sys
import romans

def verify_opt(opt):
    if opt.isnumeric() == True:
        # print("*") # print test
        return True
    #elif RomanNumerals.verify_roman(opt) == True:
    #    return True
    else:
        return False


def main():
    print("\n\n***Roman/Arabic alternator***")
    valid_opt = False
    while valid_opt == False:
        print("\nEnter an Arabic or Roman neumeral:")
        print("(or type Q to quit)\n")
        opt = input()
        if opt == "Q":
            sys.exit("\n\nThank you.")

        elif verify_opt(opt) == False:
            print("\n'{}' not recognized.".format(opt))
            continue

        elif verify_opt(opt) == True:
            # suite
            valid_opt = True

if __name__ == "__main__" : main()