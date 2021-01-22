# USE CASE:

# Our user is a BUSINESS PERSON who has to manage MULTIPLE CUSTOMERS.

# She wants to keep TRACK of how frequently SHE CONTACTS EACH CUSTOMER, so she can stay in their consciousness over time.

# One use case would be managing leads for a realtor: people give you names of friends and family who are thinking about buying a house. You'll want to periodically send them inquiries to make sure that when they decide it's time to buy they think of you.

# Another use case would be a freelance artist tracking art directors at various companies. You'd want to send regular inquiries to make sure you're on their radar.

# This exercise has two primary purposes:
# first, you're building the infrastructure to store an in-memory database of contact information, building on the work that you did in previous parts of the exercise;
# second, you're starting to think about the user interface to deal with managing the database.

# Allow the user to enter multiple customer contacts, storing the resulting dictionaries in a list.

# Provide options, in a main program loop, to view, edit, add, and delete customer contact entries

# While viewing an entry, give the user the option to log a contact, adding a contact date to the record (ala refinement 1)

class Client:
    """
    Three static methods for Records:
    verifyphone, verifyemail, verify date confirm the information input from the user is ready for storing in Database
    """
    @staticmethod
    def set_phone(p):
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

    @staticmethod
    def set_email(e):
        # slice off the last four letters
        dotcom = e[-4::1]
        
        # list of Top Level Domains that we accept
        tld_list = (".com",".org",".net",".int",".edu",".gov",".mil")

        # check for only 1 @ and valid .tld
        if e.count("@") != 1:
            raise ValueError("Must have only one @ symbol")
        elif dotcom not in tld_list:
            raise ValueError("Your provider (TLD) is not recognized")
        # returns e as a str
        return e

    @staticmethod
    def verifydate(d,m,y):   
        #swap year and day into digits
        d = int(d)
        m = int(m)
        y = int(y)
        
        try:
            outdate = datetime.date(year=y, month=m, day=d)
        except ValueError as e:
            raise ValueError("The date you entered is invalid.")

        if outdate.year > datetime.date.today().year:
            raise ValueError("Connections must be this year or earlier.")

        return outdate

    def __init__(self, f_name,l_name,phone,email,connection):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = self.set_phone(phone)
        self.email = self.set_email(email)
        self.connection = connection
        # self.key = uuid.uuid1()

class Database:
    def __init__(self):
        self.verified = False
        import datetime
        import sys
    
    #def new_client():
    # initialize inputting contact info
    # "verified" means the user has seen their input and verified its accuracy
        while self.verified == False:
            # input the employee First name, Last Name
            print("Enter the employee's personal data:")
            f_name = input("\nType First Name:\n")
            l_name = input("\nType Last Name:\n")
            phone = input("\nType Phone Number:\n")
            email = input("\nType Email Address:\n")
            startdate = (datetime.date.today(), "Contact Entered in DB")
            
            inputting = True
            inputerror = None
            while inputting:
                try:
                    new_client = Client(f_name,l_name,phone,email,startdate)
                except ValueError as e:
                    inputerror = e

                # if there are no errors, exit loop
                if inputerror == None:
                    inputting = False
                else:
                    print(inputerror)
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
        return new_client

class Interface:
    def __init__(self):
        # input what you want to do from the Options list:
        self.options = ("SEARCH", "S", "NEW", "N", "CONNECTION", "C", "EXIT", "E")

    def start(self):

        # keyword for what you're doing is "managing"
        print("*** Welcome to Client Manager ***\n\n")
        print("Youre options include:\n")
        print("Type NEW to add a new Contact")
        print("Type CONNECTION to record time with a Contact")
        manage = input("---Type an Option:---\n")

        # convert manage variable to all caps:
        manage = manage.upper()

        while manage not in self.options:
            print("\nError - option not found - please type again.")
            manage = input("---Type an Option:---\n")
            #convert manage variable to all caps:
            manage = manage.upper()
        else:
            if manage == "SEARCH":
                searchword = input("\nEnter a Searchword:\n")

            elif manage == "NEW" or "N":
                new_client = Database()
                print(new_client)
                manage = "EXIT"
            # elif manage == "CONNECTION" or "CX":
                

            elif manage == "EXIT":
                sys.exit("\nThank You")

def main():
    ui = Interface()
    ui.start()

if __name__ == "__main__" : main()