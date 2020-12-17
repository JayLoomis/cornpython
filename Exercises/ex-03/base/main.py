# Prompts the user to enter the following information for a customer contact list:
    # Last name
    # First name
    # Phone number
    # Email address
# Stores the supplied information in a dictionary with appropriately named keys
# Once stored, prints out the entry in a format that looks good to you


# Each Dict is one record. Lname, Fname, Phone, Email, and recordnum are keys.
# Each Dict identifier is in a master list.

#start with a hard code version:
def search():
    Person01 = dict(Fname="Mitch", Lname="Sorrenstein", Phone="2063461724", Email="muscles@man.com")
    print()
    print(Person01.values())

def main():
    options = ("SEARCH", "EMPLOY")
    print("Welcome to The Park Directory")
    print("You can...")
    print("SEARCH for an employee")
    print("EMPLOY a new employee")
    manage = input("---Type an Option:---\n")
    while manage not in options:
        print("\nError - please type again.")
        manage = input("---Type an Option:---\n")
    else:
        if manage == "SEARCH":
            search()
        elif manage == "EMPLOY":
            employ()
        #elif start == "FIRE":
            #fire()

if __name__ == "__main__" : main()