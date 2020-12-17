#whoopsie Doodles

#pin = " (123) 456- 7890 "
#pout = "    "
#nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#for num in pin:
#    if num in nums:
#        pout += num
#    else:
#        continue

#print(pin)
#print(pout)
#print(type(pout))

def verifyphone(p):
    startnum = p
    outnum = ""
    goodnums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for num in startnum:
        if num in goodnums:
            outnum += num
        else:
            continue
    return outnum

def main():
    print(verifyphone(input("type in a number")))
    

if __name__ == "__main__" : main()