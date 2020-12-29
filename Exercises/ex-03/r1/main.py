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
    for num in startnum:
        if num.isdigit():
            outnum += num
        else:
            continue

    if len(outnum) > 10:
        outnum = "Error:  Too many numbers."
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
        print("Error - no At Symbol")
    elif dotcom not in tld_list:
        print("not a dotcom")
    #else:
        #e = "Great"
    return e



def main():
    #working with a Sample Record:
    test_record = dict(f_name="Jane", l_name="Doe", phone="(206) 346-1724", email="Jane@Doemail.com", contdate=datetime.date.today())

    #defining options for this program
    #SEARCH is for looking up a contact - not complete in this module
    #NEW is for adding a new contact
    options = ("SEARCH", "NEW", "CONTACT", "EXIT")
    
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
            accurate = False
            while accurate == False:
                #input the employee info
                print("Enter the employee's personal data:")
                f_name = input("\nType First Name:\n")
                l_name = input("\nType Last Name:\n")
                phone = input("\nType Phone Number:\n")
                email = input("\nType Email Address:\n")
                l_contacted = {datetime.date.today(), "Contact Entered in DB"}

                #verify phone drops whatever format they have and replaces it, counts numbers
                phone = verifyphone(phone)

                #verify TLD and that there is an @ symbol.
                #currently no verification for multiple @ symbols.
                email = verifyemail(email)

                a_record = dict(f_name=f_name, l_name=l_name, phone=phone, email=email, l_contacted=l_contacted)
                
                #print a verification of the Dictionary values:
                print("\nYour new employee data is:")
                for data in a_record.values():
                    print(data)

                #loop for option to re-input data
                checkaccurate = input("\nIs this accurate? Y/N\n")
                checkaccurate = checkaccurate.upper()
                if checkaccurate == "Y":
                    accurate = True
        elif manage == "CONTACT":
            print("\nEnter date of Conact")
            whencont = input("format: YYYY-M-D\n")
            notecont = input("\nAdd any notes about your contact\n")
            print(f"You're entering {notecont} as happening on {whencont}")
            print("Is this correct? Y/N")
        elif manage == "EXIT":
            sys.exit("\nFINE, THEN YOU'RE FIRED!")

if __name__ == "__main__" : main()
