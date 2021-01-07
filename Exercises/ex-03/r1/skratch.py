#Skratch
import random
import datetime

def verifyday(d):
    if d.isdigit() == False:
        raise ValueError("Please enter a numeral")
    elif int(d) > 31:
        raise ValueError("Day number is too high.")
    elif int(d) < 1:
        raise ValueError("Day must be between 1 and 31.")

    return d

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
    if int(y) > datetime.datetime.today().year:
        raise ValueError("Date cannot be in the future.")
    else:
        # returns the year
        return y

def main():
    contactdate = None
    baddate = None
    
    verified = False
    while verified == False:
        # input the date of contact
        print("\nDid you make this contact today?  Y/N")
        inputtoday = input()
        inputtoday = inputtoday.upper()
        if inputtoday == "Y":
            contactdate = datetime.date.today()
        else:
            # input the day and check to make sure is between 1 and 31
            inputting = True
            while inputting:
                d = input("Day?\n")
                try:
                    #verifies day is between 1 and 31
                    d = verifyday(d)
                except ValueError as e:
                    baddate = e
                if baddate == None:
                    inputting = False
                else:
                    print(baddate)
                    baddate = None
                    continue
            
            # get and check the month
            inputting = True
            while inputting:
                m = input("Month?\n")
                try:
                    # verify month takes in a STR and returns a format code
                    monthformat = verifymonth(m)
                except ValueError as e:
                    baddate = e
                if baddate == None:
                    print(monthformat)
                    inputting = False
                else:
                    print(baddate)
                    baddate = None
                    continue

            # get and check to make sure the year isn't in the future
            inputting = True
            while inputting:
                y = input("Year?\n")
                try:
                    y = verifyyear(y)
                except ValueError as e:
                    baddate = e
                if baddate == None:
                    inputting = False
                else:
                    print(baddate)
                    baddate = None
                    continue

        # just here to show that the input is working.
        print(d, monthformat, y)
        # build the date as a datetime object
        # https://stackoverflow.com/questions/466345/converting-string-into-datetime
        
        # Input notes and verify the information input
        contactnote = input("\nAdd any notes about your contact\n")
        print(f"\nYou're entering:\n--> {contactnote}\nas happening on:  {contactdate}")
        
        #loop for option to re-input data
        checkaccurate = input("\nIs this accurate? Y/N\n")
        checkaccurate = checkaccurate.upper()
        if checkaccurate == "Y":
            verified = True


if __name__ == "__main__" : main()