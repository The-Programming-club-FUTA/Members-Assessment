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
    
    while i < len(s):
        if i + 1 < len(s) and numerals[s[i]] < numerals[s[i + 1]]:
            output += (numerals[s[i + 1]] - numerals[s[i]])
            i += 2
        else:
            output += numerals[s[i]]
            i += 1
    return output
