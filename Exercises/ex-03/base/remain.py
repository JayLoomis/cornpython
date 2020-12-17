# Prompts the user to enter the following information for a customer contact list:
    # Last name
    # First name
    # Phone number
    # Email address
# Stores the supplied information in a dictionary with appropriately named keys
# Once stored, prints out the entry in a format that looks good to you


# Each Dict is one record. Lname, Fname, Phone, Email, and recordnum are keys.
# Each Dict identifier is in a master list.

import sys

def search():
    print("SEARCH is not available at this time.\n\n")
    main()

def verifyphone(p):
    #initialize starting input:  p
    startnum = p
    #initialize an empty string to catch the number we need.
    outnum = ""
    #goodnums is a list of just the digits we want to accept.
    goodnums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    #for loop goes through their string and adds only the digits of goodnums to the output variable
    for num in startnum:
        if num in goodnums:
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
    if "@" not in e:
        print("Error - no At Symbol")
    elif dotcom not in tld_list:
        print("not a dotcom")
    #else:
        #e = "Great"
    return e

def main():
    #defining options for this program
    #SEARCH is for looking up an Employee - not complete in this module
    #EMPLOY is for hiring / adding someone to the DB
    options = ("SEARCH", "EMPLOY", "EXIT")
    print("Welcome to The Park Directory")
    
    #input what you want to do (in this case Employ)
    #keyword for what you're doing is "managing"
    print("Type EMPLOY to add a new employee")
    manage = input("---Type an Option:---\n")

    #convert manage variable to all caps:
    manage = manage.upper()

    while manage not in options:
        print("\nError - please type again.")
        manage = input("---Type an Option:---\n")
        #convert manage variable to all caps:
        manage = manage.upper()
    else:
        if manage == "SEARCH":
            search()
        elif manage == "EMPLOY":
            accurate = False
            while accurate == False:
                #input the employee info
                print("Enter the employee's personal data:")
                f_name = input("\nType First Name:\n")
                l_name = input("\nType Last Name:\n")
                phone = input("\nType Phone Number:\n")
                email = input("\nType Email Address:\n")

                #verify phone drops whatever format they have and replaces it, counts numbers
                phone = verifyphone(phone)

                #verify TLD and that there is an @ symbol.
                #currently no verification for multiple @ symbols.
                email = verifyemail(email)

                a_record = dict(f_name=f_name, l_name=l_name, phone=phone, email=email)
                
                #print a verification of the Dictionary values:
                print("\nYour new employee data is:")
                for data in a_record.values():
                    print(data)

                #loop for option to re-input data
                checkaccurate = input("\nIs this accurate? Y/N\n")
                checkaccurate = checkaccurate.upper()
                if checkaccurate == "Y":
                    accurate = True
        #elif start == "FIRE":
            #fire()
        elif manage == "EXIT":
            sys.exit("\nFINE, THEN YOU'RE FIRED!")

if __name__ == "__main__" : main()