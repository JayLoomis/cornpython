#Skratch
import random
import datetime

def verifyphone(p):
    #initialize starting input:  p
    startnum = p
    #initialize an empty string to catch the number we need.
    outnum = ""

    #for loop goes through their string and adds only the digits of goodnums to the output variable
    for digit in startnum:
        if digit.isdigit():
            outnum += digit
        else:
            continue

    if len(outnum) != 10:
        raise ValueError("Incorrect number of digits for a phone number.")
    else:
        outnum = "({}) {}-{}".format(outnum[:3],outnum[3:6],outnum[6:])

    return outnum

def verifymonth(m):   
    # 
    if m.isdigit():
        dateformat = "%m"
    elif len(m) == 3:
        dateformat = "%b"
    elif len(m) > 3:
        dateformat = "%B"
    else:
        raise ValueError("Month not recognized.")
    # returns the month as an strftime format
    # https://strftime.org/
    return dateformat

def verifyyear(y):   
    # 
    if y > datetime.date.year():
        raise ValueError("Date is in the future")
    else:
        # returns the year
        return y

def main():
    contactdate = None
    badmonth = None
    wrongyear = None

    verified = False
    while verified == False:
        # input the date of contact
        print("\nDid you make this contact today?  Y/N")
        inputtoday = input()
        inputtoday = inputtoday.upper()
        if inputtoday == "Y":
            contactdate = datetime.date.today()
        else:
            datecheck = False
            while datecheck == False:
                # get the day
                d = input("Day?\n")
                # get and check the month
                inputting = True
                while inputting:
                    m = input("Month?\n")
                    try:
                        # verify month takes in and formats a str
                        monthformat = verifymonth(m)
                    except ValueError as e:
                        badmonth = e
                    if badmonth == None:
                        inputting = False
                    else:
                        print(badmonth)
                        badmonth = None
                        continue

                # get and check to make sure the year isn't in the future
                inputting = True
                while inputting:
                    y = input("Year?\n")
                    try:
                        verifyyear(y)
                    except ValueError as e:
                        wrongyear = e
                    if wrongyear == None:
                        inputting = False
                    else:
                        print(wrongyear)
                        wrongyear = None
                        continue

# https://stackoverflow.com/questions/466345/converting-string-into-datetime

        contactnote = input("\nAdd any notes about your contact\n")
        print(f"\nYou're entering:\n--> {contactnote}\nas happening on:  {contactdate}")
        
        #loop for option to re-input data
        checkaccurate = input("\nIs this accurate? Y/N\n")
        checkaccurate = checkaccurate.upper()
        if checkaccurate == "Y":
            verified = True


if __name__ == "__main__" : main()