import uuid

class Client:
    """
    Three static methods for Records:
    verifyphone, verifyemail, verify date confirm the information input from the user is ready for storing in Database
    """

    @staticmethod
    def getFields (self):
        fields_description = {f_name: "First Name", l_name : "Last Name", phone : "Phone number" , email : "Email address" , connection : "This field is a Collection of datetime objects tied to a Notes field."}
        fields_count = len(fields_description)
        fields = [fields_description, fields_count]
        return fields

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

    def verifydate(self, d,m,y):   
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
        self.f_name = f_name.capitalize()
        self.l_name = l_name.capitalize()
        self.phone = set_phone(phone)
        self.email = set_email(email)
        self.connection = connection
        self.key = uuid.uuid1()