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
        self.phone = set_phone(phone)
        self.email = set_email(email)
        self.connection = connection
        self.key = uuid.uuid1()

class Database:
    def new_client()
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

class Interface:
    options = ("SEARCH", "S", "NEW", "N", "CONNECTION", "C", "EXIT", "E")
    
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
            searchword = input("\nEnter a Searchword:\n")

        elif manage == "NEW":
            database.new()

        elif manage == "CONNECTION" or "CX":
            database.connection()

        elif manage == "EXIT":
            sys.exit("\nThank You")

def main():


if __name__ == "__main__" : main()