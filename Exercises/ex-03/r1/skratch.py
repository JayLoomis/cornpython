#Skratch
import random
import datetime

def effin():
    x = 2
    y = 8
    thing = 'word {0:19} {0:<09}'
    print(thing.format(x,y))
    print(type(thing))

def jeffin():
    accurate = False
    while accurate == False:
        # input the date of contact
        print("\nDid you make this contact today?  Y/N")

        inputtoday = input()
        inputtoday = inputtoday.upper()
        if inputtoday == "Y":
            contactdate = datetime.date.today()
        else:
            contactdate = []
            contactdate.append(input("Year?\n"))
            contactdate.append(input("Month?\n"))
            contactdate.append(input("Day?\n"))

        #verifydate returns accurate date or 
#        contactdate = verifydate(contactdate)

        contactnote = input("\nAdd any notes about your contact\n")
        print(f"\nYou're entering:\n{contactnote}\nas happening on: {contactdate}")
        
        print(type(contactdate))

        #loop for option to re-input data
        checkaccurate = input("\nIs this accurate? Y/N\n")
        checkaccurate = checkaccurate.upper()
        if checkaccurate == "Y":
            accurate = True

def main():
    jeffin()

if __name__ == "__main__" : main()
