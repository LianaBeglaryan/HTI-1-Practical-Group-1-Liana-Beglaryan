def romanToInt(s) -> int:
        romanHash = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        value = 0
        previous = number = romanHash[s[0]]
        for r in s[1:]:
            value = romanHash[r]
            if value > previous:
                number = number + value - 2 * previous
            else:
                number = number + value
            previous = value
        return number

s=input("tpel taretiv: ")        
romanToInt(s)
