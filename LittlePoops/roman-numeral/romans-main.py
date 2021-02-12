import romans

def verify_num(opt):
    if opt.isnumeric() == True:
        return True
    else:
        return False


def main():
    print("\n\n***Roman/Arabic translator***")
    translating = True
    romantique = romans.RomanNumerals()
    while translating == True:
        print("\nEnter an Arabic or Roman neumeral:")
        print("(or type Q to quit)\n")
        num = input()
        num = num.upper()
        if num == "Q":
            print("\n\nThank you.")
            translating = False

        elif num.isnumeric():
            if int(num) > 9999:
                print("Too large for Roman calculations")
                continue
            else:
                conversion = romantique.arabic_to_roman(num)
                print(conversion)
                continue

        elif romantique.verify_roman(num):
            conversion = romantique.roman_to_arabic(num)
            print(conversion)
            continue



if __name__ == "__main__" : main()