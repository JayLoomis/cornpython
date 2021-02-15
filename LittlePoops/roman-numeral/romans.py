class RomanNumerals:
    
    def arabic_to_roman(self, arabic):
        pass

    def roman_to_arabic(self, roman):
        # turn the string we recieve into a list
        self.roman = self.roman
        chars = []
        for char in self.roman:
            chars.append(char)

        # initialize a new list for thousands, hundreds, tens, and ones
        m = []
        cd = []
        xl = []
        iv = []

        """
        now that we have one big list of every letter, we can check what the first one is,
        we move it to the correct list:  thousands, hundreds, tens, or ones
        once it's moved, we delete it, so we're always just looking at the first character
        in roman numerals each break after the thousands starts with only one of two letters:
        hundreds starts with a C or a D
        tens starts with an X or L
        ones alway start with a I or V
        """
        while len(chars)>0:
            if chars[0] == "M":
                m.append(chars[0])
                del chars[0]
            elif chars[0] == "C":
                break
            elif chars[0] == "D":
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            if chars[0] == "C":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "D":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "M":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "X":
                break
            elif chars[0] == "L":
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            if chars[0] == "X":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "L":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "C":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "I":
                break
            elif chars[0] == "V":
                break

        while len(chars)>0:
            if chars[0] == "I":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "V":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "X":
                iv.append(chars[0])
                del chars[0]

        """
        now that we have four discrete lists of thousands, hundreds, tens, ones
        we can create logic to capture which value it is.
        --> to deal with 4 and 9 (subtractive values) <--
        start first by checking which letter is the first letter
        if the len is 1 it's 1
        if the second list item is a letter it must be a 2, 4 or 9
        if the list has a third value it can only be 3
        for values 5-8 you simply count the len of the list
        as the pattern is always A AB ABB ABBB

        the structure is the same for hundreds, tens and ones

        thousands only has one letter, so you simply multiply 1k by len
        """

        # test print the lists for troubleshooting
        # print("m is: ", m)
        # print("cd is: ",cd)
        # print("xl is: ",xl)
        # print("iv is: ",iv)

        thousands = 1000 * len(m)

        hundreds = 0
        if len(cd) > 0:
            if cd[0] == "C":
                if len(cd) == 1:
                    hundreds = 100
                elif cd[1] == "C":
                    hundreds = 200
                elif cd[1] == "D":
                    hundreds = 400
                elif cd[1] == "M":
                    hundreds = 900
                elif cd[2] == "C":
                    hundreds = 300

            elif cd[0] == "D":
                if len(cd) == 1:
                    hundreds = 500
                elif len(cd) == 2:
                    hundreds = 600
                elif len(cd) == 3:
                    hundreds = 700
                elif len(cd) == 4:
                    hundreds = 800


        tens = 0
        if len(xl) > 0:
            if xl[0] == "X":
                if len(xl) == 1:
                    tens = 10
                elif xl[1] == "X":
                    tens = 20
                elif xl[1] == "L":
                    tens = 40
                elif xl[1] == "C":
                    tens = 90
                elif xl[2] == "X":
                    tens = 30

            elif xl[0] == "L":
                if len(xl) == 1:
                    tens = 50
                elif len(xl) == 2:
                    tens = 60
                elif len(xl) == 3:
                    tens = 70
                elif len(xl) == 4:
                    tens = 80

        ones = 0
        if len(iv) > 0:
            if iv[0] == "I":
                if len(iv) == 1:
                    ones = 1
                elif iv[1] == "I":
                    ones = 2
                elif iv[1] == "V":
                    ones = 4
                elif iv[1] == "X":
                    ones = 9
                elif iv[2] == "I":
                    ones = 3

            elif iv[0] == "V":
                if len(iv) == 1:
                    ones = 5
                elif len(iv) == 2:
                    ones = 6
                elif len(iv) == 3:
                    ones = 7
                elif len(iv) == 4:
                    ones = 8

        arabic = thousands + hundreds + tens + ones
        return arabic

    def verify_roman(self, roman):
        # turn the string we recieve into a list
        self.roman = roman
        chars = []
        for char in self.roman:
            chars.append(char)

        # initialize a new list for thousands, hundreds, tens, and ones
        m = []
        cd = []
        xl = []
        iv = []

        """
        now that we have one big list of every letter, we can check what the first one is,
        we move it to the correct list:  thousands, hundreds, tens, or ones
        once it's moved, we delete it, so we're always just looking at the first character
        in roman numerals each break after the thousands starts with only one of two letters:
        hundreds starts with a C or a D
        tens starts with an X or L
        ones alway start with a I or V
        """
        while len(chars)>0:
            if chars[0] == "M":
                m.append(chars[0])
                del chars[0]
            elif chars[0] == "C":
                break
            elif chars[0] == "D":
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            if chars[0] == "C":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "D":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "M":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "X":
                break
            elif chars[0] == "L":
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            if chars[0] == "X":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "L":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "C":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "I":
                break
            elif chars[0] == "V":
                break

        while len(chars)>0:
            if chars[0] == "I":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "V":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "X":
                iv.append(chars[0])
                del chars[0]

        cd = "".join(cd)
        xl = "".join(xl)
        iv = "".join(iv)

        hundreds = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["I","II","III","IV","V","VI","VII","VIII","IX"]

        if len(m) > 0:
            for m in m:
                if m != "M":
                    raise ValueError("Incorrect Thousands")

        if len(cd) > 0:
            if cd not in hundreds:
                raise ValueError("Incorrect Hundreds")

        elif len(xl) > 0:
            if xl not in tens:
                raise ValueError("Incorrect Hundreds")
        
        elif len(iv) > 0:
            if iv not in ones:
                raise ValueError("Incorrect Hundreds")
        
        else:
            return True