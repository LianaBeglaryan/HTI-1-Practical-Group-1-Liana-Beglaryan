def roman_to_int(s):
        roman = {'I':1 ,'V':5 ,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        previous = number = roman[s[0]]
        for r in s[1:]:
            value = roman[r]
            if value > previous:
                number = number + value - 2 * previous        
            number = number + value
            previous = value
        return number
       
s = input("enter a date: ")        
print(roman_to_int(s))
