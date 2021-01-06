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
    main()

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

def verifyemail(e):
    #slice off the last four letters
    dotcom = e[-4::1]
    
    #list of Top Level Domains that don't suck
    tld_list = (".com",".org",".net",".int",".edu",".gov",".mil")

    #check for @ and .something
    if e.count("@") != 1:
        raise ValueError("Must have ONE @ symbol")
    elif dotcom not in tld_list:
        raise ValueError("Your TLD is nor recognized")
    
    return e

def verifydate(y,m,d):   
    #THIS DON'T WORK - NEED TO JUST DO ERRORS. DUH. 
    #swap year and day into digits
    y = int(y)
    d = int(d)
    m = m.lower()


def main():
    #working with a Sample Record:
    test_record = dict(f_name="Jane", l_name="Doe", phone="(206) 346-1724", email="Jane@Doemail.com", contactdate={datetime.date.today(), ""})

    #defining options for this program
    #SEARCH is for looking up a contact - not complete in this module
    #NEW is for adding a new contact
    options = ("SEARCH", "NEW", "CONTACT", "EXIT")
    
    #setting up some errors
    phoneerror = None
    emailerror = None

    #input what you want to do (in this case NEW to add a contact)
    #keyword for what you're doing is "managing"
    print("Type NEW to add a client")
    print("Type CONTACT to record contact with a client")
    manage = input("---Type an Option:---\n")

    #convert manage variable to all caps:
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
            #initialize inputting contact info, verified means the user has seen their input and verified its accuracy
            verified = False
            while verified == False:

                #input the employee First name, Last Name
                print("Enter the employee's personal data:")
                f_name = input("\nType First Name:\n")
                l_name = input("\nType Last Name:\n")

                #inputting employee phone info
                inputting = True
                while inputting:
                    phone = input("\nType Phone Number:\n")
                    # verifyphone() drops whatever format they have and replaces it, counts numbers
                    try:
                        # If verifyphone() generates an error it is stored in phoneerror (initialized line 80)
                        phone = verifyphone(phone)
                    except ValueError as e:
                        phoneerror = e
                    # if there are no errors, exit loop
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
                a_record = dict(f_name=f_name, l_name=l_name, phone=phone, email=email, startdate=startdate)
                
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

        elif manage == "CONTACT":
            accurate = False
            while accurate == False:
                # input the date of contact
                print("\nDid you make this contact today?  Y/N")


                inputtoday = input()
                inputtoday = inputtoday.upper()
                if inputtoday == "Y":
                    contactdate = datetime.date.today()
                else:
                    datecheck = False
                    while datecheck == False:
                        contactdate = []
                        contactdate.append(input("Year?\n"))
                        contactdate.append(input("Month?\n"))
                        contactdate.append(input("Day?\n"))

                        #verifydate returns accurate date or specific error problems
                        if type(verifydate(contactdate)) == datetime.date:
                            contactdate = verifydate(contactdate)
                            datecheck = True
                        else:
                            print(verifydate(contactdate))
                            



                contactnote = input("\nAdd any notes about your contact\n")
                print(f"\nYou're entering:\n--> {contactnote}\nas happening on:  {contactdate}")
                
                #loop for option to re-input data
                checkaccurate = input("\nIs this accurate? Y/N\n")
                checkaccurate = checkaccurate.upper()
                if checkaccurate == "Y":
                    accurate = True
                
        elif manage == "EXIT":
            sys.exit("\nThank You")

if __name__ == "__main__" : main()
