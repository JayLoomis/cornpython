
# Write a function that takes a positive integer as an argument &
# returns a Boolean indicating whether the argument is a power of three.

# Hint: you might want to use recursion for this, which we haven't talked about yet. Exciting!

def threepower(x,p):
    p = int(p)
    if x ** 3 == p:
        return True
    elif x >= p:
        return False
    elif x ** 3 < p:
        x += 1
        return threepower(x,p)


def main():
    trying = True
    while trying:
        p = input("Gimme a number:\n")
        if p.isdigit():
            if threepower(1,p) == True:
                print(f"{p} is a power of 3.")
                continue
            else:
                print("Nope.  Try again?")
                continue
        elif p == "Done" or "done":
            trying = False
        elif p.isdigit() == False:
            print("I said a number.\nTry Again:\n")
            continue


if __name__ == "__main__" : main()