class RomanNumerals:
    
    def arabic_to_roman(self, arabic):
        pass

    def roman_to_arabic(self, roman):
        if len(roman) == 0:
            return 0
        elif roman.endswith("I",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+1
        elif roman.endswith("IV",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+4
        elif roman.endswith("V",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+5
        elif roman.endswith("IX",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+9
        elif roman.endswith("X",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+10
        elif roman.endswith("XL",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+40
        elif roman.endswith("L",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+50
        elif roman.endswith("XC",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+90
        elif roman.endswith("C",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+100
        elif roman.endswith("CD",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+400
        elif roman.endswith("D",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+500
        elif roman.endswith("CM",-2):
            roman = roman[:-2]
            return self.roman_to_arabic(roman)+900
        elif roman.endswith("M",-1):
            roman = roman[:-1]
            return self.roman_to_arabic(roman)+1000

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
            elif chars[0] != "M":
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            cdm = ["C","D","M"]
            if chars[0] == "C":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "D":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] == "M":
                cd.append(chars[0])
                del chars[0]
            elif chars[0] not in cdm:
                break
        # test print of chars
        # print(chars, "\n")

        while len(chars)>0:
            xlc = ["X","L","C"]
            if chars[0] == "X":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "L":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] == "C":
                xl.append(chars[0])
                del chars[0]
            elif chars[0] not in xlc:
                break

        while len(chars)>0:
            ivx = ["I","V","X"]
            if chars[0] == "I":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "V":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] == "X":
                iv.append(chars[0])
                del chars[0]
            elif chars[0] not in ivx:
                break

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