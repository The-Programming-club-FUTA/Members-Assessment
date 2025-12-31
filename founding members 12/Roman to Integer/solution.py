def romanToInt(self, s: str) -> int:
    
    numerals ={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    output = 0
    i = 0
    
    while(i < (len(s))):
        j = i
        if j < len(s) and numerals[s[i]] < numerals[s[j]]:
                output += (numerals[s[j]] - numerals[s[i]])
                i += 2
                continue
        output += numerals[s[i + 1]]
        i += 1
    return output
