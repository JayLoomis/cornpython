import datetime
import sys
import database

class Interface:

    def __init__(self):
        # input what you want to do from the Options list:
        self.options = ("NEW", "N", "CONNECTION", "C", "EXIT", "E")

    def start(self):
        """
        Intialize Client Tracker interface.  Show the user what options they have.
        """
        # keyword for what you're doing is "managing"
        print("*** Welcome to Client Tracker ***\n\n")
        print("Youre options include:\n")
        print("Type NEW to add a new Contact")
        print("Type CONNECTION to record time with a Contact")
        optionpick = input("\n---Type an Option:---\n")
        """
        Program runs on While loop until Exit is chosen by user.  Loop restarts if an option not listed in self.options built in constructor.
        """
        # convert optionpick variable to all caps:
        optionpick = optionpick.upper()
        executing = True
        while executing == True:
            if optionpick not in self.options:
                print("\nError - option not found - please type again.")
                optionpick = input("---Type an Option:---\n")
                #convert optionpick variable to all caps:
                optionpick = optionpick.upper()
                continue
            elif optionpick == "NEW" or "N":
                """
                New is for inputting a new client, by default a new client has a connection date of the day you enter the client with the notes "Contact Entered into DB"
                
                "verified" means the user has seen their input and verified its accuracy
                """
                
                # initialize inputting contact info                
                verified = False
                while verified == False:
                    inputting = True
                    inputerror = None
                    while inputting:
                        # input the employee First name, Last Name
                        print("Enter the employee's personal data:")
                        f_name = input("\nType First Name:\n")
                        f_name = f_name.capitalize()
                        l_name = input("\nType Last Name:\n")
                        l_name = l_name.capitalize()
                        phone = input("\nType Phone Number:\n")
                        email = input("\nType Email Address:\n")
                        startdate = [datetime.date.today(), "Contact Entered in DB"]
                        
                        # capture errors from database or None
                        try:
                            inputerror = database.Database.new_obj_check(f_name,l_name,phone,email,startdate)
                        except ValueError as e:
                            inputerror = e

                        # if there are no errors, exit loop
                        if inputerror == None:
                            inputting = False
                        else:
                            print(inputerror)
                            print("\nplease re-enter:")
                            inputerror = None
                            continue

                    #print a verification of the Dictionary values:
                    print("\nYour new employee data is:")
                    print(f_name, " ", l_name)
                    print("Phone #:  ", phone)
                    print("Email is:  ", email)

                    #loop for option to re-input data / Verify Accuracy
                    checkaccurate = input("\nIs this accurate? Y/N\n")
                    checkaccurate = checkaccurate.upper()
                    if checkaccurate == "Y":
                        verified = True
                    else:
                        continue
                # Database.enter(new_client_check)

            elif optionpick == "CONNECTION" or "CX":
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

            elif optionpick == "EXIT":
                sys.exit("\nThank You")