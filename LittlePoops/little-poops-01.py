# Write a function that takes a positive integer as an argument &
# returns a Boolean indicating whether the argument is a power of three.

# Hint: you might want to use recursion for this, which we haven't talked about yet. Exciting!

def threepower(x,p):
    p = int(p)
    if x ** 3 == p:
        return True
    elif x ** 3 > p:
        return False
    elif x ** 3 < p:
        x += 1
        threepower(x,p)


def main():
    p = input("Gimme a number:\n")
    trying = True
    while trying:
        if p.isdigit():
            trying = False
            if threepower(1,p) == True:
                print("yeah that worked.")
            else:
                print("Nope.")

        else:
            print("I said a number.\nTry Again:\n")
            continue

if __name__ == "__main__" : main()