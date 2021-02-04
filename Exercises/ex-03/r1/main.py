#Change your program created in exercise 3 to 
#add a field to the record (item to the dictionary) that holds a list of contact records.

#When the user contacts a customer, they will need to add that interaction to the customer record.
#Your dictionary should track a list of customer interactions, 
#by making a new dictionary item that holds a list of interaction records.
#Each should have the date and time of the interaction and a note that the user enters.

#Come up with an appropriate user interface whereby the user can 
  #add, view, or delete customer interactions from the customer record.

#Make functions to perform the 
  #adding and deleting of customer interactions.

#Use the standard Python datetime module
#to get the current time when the user adds a customer interaction.
#Decide the best way to store the datetime information in your list.

import sys
import datetime

def search():
    print("SEARCH is not available at this time.\n\n")

def verifyphone(p):
    # initialize starting input:  p
    startnum = p
    # initialize an empty string to catch the number we need.
    outnum = ""

    # for loop goes through their string and adds only the digits of goodnums to the output variable
    for digit in startnum:
        if digit.isdigit():
            outnum += digit
        else:
            continue
    # check to make sure the phone number is 10 digits long
    if len(outnum) != 10:
        raise ValueError("Incorrect number of digits for a phone number.")
    else:
        outnum = "({}) {}-{}".format(outnum[:3],outnum[3:6],outnum[6:])
    # returns outnum as string
    return outnum

def verifyemail(e):
    # slice off the last four letters
    dotcom = e[-4::1]
    
    # list of Top Level Domains that we accept
    tld_list = (".com",".org",".net",".int",".edu",".gov",".mil")

    # check for only 1 @ and valid .tld
    if e.count("@") != 1:
        raise ValueError("Must have ONE @ symbol")
    elif dotcom not in tld_list:
        raise ValueError("Your TLD is nor recognized")
    # returns e as a str
    return e

def verifydate(d,m,y):   
    #swap year and day into digits
    d = int(d)
    m = int(m)
    y = int(y)
    
    # outdate = datetime.date(year=y, month=m, day=d)

    try:
        outdate = datetime.date(year=y, month=m, day=d)
    except ValueError as e:
        raise ValueError("The date you entered is invalid.")

    if outdate.year > datetime.date.today().year:
        raise ValueError("Connections must be this year or earlier.")

    return outdate

def main():
    # working with a Sample Record:
    # test_record = dict(f_name="Jane", l_name="Doe", 
        # phone="(206) 346-1724", email="Jane@Doemail.com", 
        # contactdate={datetime.date.today():""})

    # working with a Sample Record (not using the dict() constructor)
    test_record = {"f_name" : "Jane",
                   "l_name" : "Doe",
                   "phone" : "(206) 346-1724",
                   "email" : "Jane@Doemail.com",
                   "contactdate" : {datetime.date.today().strftime("%Y%m%d"):""}}

    # defining options for this program
    # SEARCH is for looking up a contact - not complete in this module
    # NEW is for adding a new contact
    options = ("SEARCH", "NEW", "CONNECTION", "EXIT", "CX")
    
    #setting up some errors
    phoneerror = None
    emailerror = None

    # input what you want to do (in this case NEW to add a contact)
    # keyword for what you're doing is "managing"
    print("Type NEW to add a new Contact")
    print("Type CONNECTION to record time with a Contact")
    manage = input("---Type an Option:---\n")

    # convert manage variable to all caps:
    manage = manage.upper()

    while manage not in options:
        print("\nError - option not found - please type again.")
        manage = input("---Type an Option:---\n")
        #convert manage variable to all caps:
        manage = manage.upper()
    else:
        if manage == "SEARCH":
            search()

        elif manage == "NEW":
            # initialize inputting contact info
            # "verified" means the user has seen their input and verified its accuracy
            verified = False
            while verified == False:
                # input the employee First name, Last Name
                print("Enter the employee's personal data:")
                f_name = input("\nType First Name:\n")
                l_name = input("\nType Last Name:\n")

                # inputting employee phone info
                inputting = True
                while inputting:
                    phone = input("\nType Phone Number:\n")
                    # verifyphone() drops whatever format they have and replaces it, counts numbers
                    try:
                        # If verifyphone() generates an error it is stored in phoneerror
                        phone = verifyphone(phone)
                    except ValueError as e:
                        phoneerror = e
                    # if checks there are no errors, exit loop
                    if phoneerror == None:
                        inputting = False
                    else:
                        print(phoneerror)
                        phoneerror = None
                        continue

                inputting = True
                while inputting:
                    email = input("\nType Email Address:\n")
                    # verifyemail() checks for 1 @ and a set of acceptable TLD options
                    try:
                        email = verifyemail(email)
                    except ValueError as e:
                        emailerror = e

                    # if there are no errors, exit loop
                    if emailerror == None:
                        inputting = False
                    else:
                        print(emailerror)
                        emailerror = None
                        continue

                # This only captures when the record is initialized
                startdate = {datetime.date.today(), "Contact Entered in DB"}

                # sample fake record!
                a_record = {"f_name" : f_name,
                            "l_name" : l_name,
                            "phone" : phone,
                            "email" : email,
                            "startdate" : startdate}
                
                #print a verification of the Dictionary values:
                print("\nYour new employee data is:")
                print(a_record["f_name"], " ", a_record["l_name"])
                print("Phone #:  ", a_record["phone"])
                print("Email is:  ", a_record["email"])

                #loop for option to re-input data / Verify Accuracy
                checkaccurate = input("\nIs this accurate? Y/N\n")
                checkaccurate = checkaccurate.upper()
                if checkaccurate == "Y":
                    verified = True

        elif manage == "CONNECTION" or "CX":
            verified = False
            while verified == False:
                # input the date of encounter with Contact
                print("\nDid you make this contact today?  Y/N")
                inputtoday = input()
                inputtoday = inputtoday.upper()
                if inputtoday == "Y":
                    newcontactdate = datetime.date.today()
                else:
                    datechecked = False
                    while datechecked == False:
                        d = (input("Day?\nMust be two digits\n"))
                        m = (input("Month?\nMust be two digits\n"))
                        y = (input("Year?\n"))
                        #verifydate returns accurate date or specific error problems
                        feedbackerror = None
                        try:
                            newcontactdate = verifydate(d,m,y)
                        except ValueError as e:
                            feedbackerror = e
                            # newcontactdate = newcontactdate.strftime()

                        # if there are no errors, exit loop
                        if feedbackerror == None:
                            datechecked = True
                        else:
                            print(feedbackerror)
                            feedbackerror = None
                            continue
                # ask them for any notes about the connection
                newcontactnote = input("\nAdd any notes about your contact\n")
                # show it to them so they can verify it
                print(f"\nYou're entering:\n--> {newcontactnote}\nas happening on:  {newcontactdate}")
                # loop for option to re-input data
                checkaccurate = input("\nIs this accurate? Y/N\n")
                checkaccurate = checkaccurate.upper()
                if checkaccurate == "Y":
                    verified = True
                
                # append the new connection to test_record
                test_record["contactdate"][newcontactdate]=newcontactnote
                print(test_record)

        elif manage == "EXIT":
            sys.exit("\nThank You")

if __name__ == "__main__" : main()
