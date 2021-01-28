# Write a function that takes a positive integer as an argument &
# returns a Boolean indicating whether the argument is a power of three.

# Hint: you might want to use recursion for this, which we haven't talked about yet. Exciting!

# 3, 9, 27, 81...

def threepower(x,p):
    if p < 3:
        return False
    elif p == (3 ** x):
        return True
    elif p > (3 ** x):
        x += 1
        return threepower(x,p)
    elif p < (3 ** x):
        return False

def main():
    playing = True
    while playing:
        power = input("Gimme a number:\n")
        digits = True
        if power.isdigit():
            power = int(power)
            if threepower(2,power) == True:
                print(f"{power} is a power of 3.")
                continue
            else:
                print(f"{power} is not a power of 3.")
                continue
        elif power.isdigit() == False:
            print("You must provide a number.")
            print("Or type DONE to exit.")
            if power.upper() == 'DONE':
                playing = False
            else:
                continue

if __name__ == "__main__" : main()