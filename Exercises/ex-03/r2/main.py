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

class Records:
    """
    Three static methods for Records:
    verifyphone, verifyemail, verify date confirm the information input from the user is ready for storing in Database
    """
    @staticmethod
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

    @staticmethod
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

    record = {"f_name" = f_name,
              "l_name" = l_name,
              "phone" = phone,
              "email" = email,
              "connection" = (con_date, con_notes) }



class Database:


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
            database.search()

        elif manage == "NEW":
            database.new()

        elif manage == "CONNECTION" or "CX":
            database.connection()

        elif manage == "EXIT":
            sys.exit("\nThank You")

def main():


if __name__ == "__main__" : main()