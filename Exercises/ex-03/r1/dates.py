#Skratch
import random
import datetime

def get_valid_day(d):
    if d.isdigit() == False:
        raise ValueError("Please enter a numeral")
    elif int(d) > 31:
        raise ValueError("Day number is too high.")
    elif int(d) < 1:
        raise ValueError("Day must be between 1 and 31.")

    return d

def get_valid_month(m):
    smallmonths = ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
    bigmonths = ("january","february","march","april","may","june","july","august","september","october","november","december")
    if m.isdigit():
        m = int(m)
        if m < 0 or m > 13:
            raise ValueError("Month out of Range")
        else:
            return str(m)
    elif m.lower() in smallmonths:
        m = smallmonths.index(m.lower()) + 1
        return str(m)
    elif m.lower() in bigmonths:
        m = bigmonths.index(m) + 1
        return str(m)
    else:
        raise ValueError("Month not recognized")


def get_valid_year(y):   
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
                    d = get_valid_day(d)
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
                    # verify month takes in a STR and returns a tuple
                    # first is the 
                    get_valid_month(m)
                except ValueError as e:
                    baddate = e
                if baddate == None:
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
                    y = get_valid_year(y)
                except ValueError as e:
                    baddate = e
                if baddate == None:
                    inputting = False
                else:
                    print(baddate)
                    baddate = None
                    continue

        # just here to show that the input is working.

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