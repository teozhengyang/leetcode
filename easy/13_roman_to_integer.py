def romanToInt(self, s: str) -> int:
    # Dictionary to map Roman numerals to integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # start from the last character
    prev_no = roman_to_int[s[-1]]
    total = prev_no
    
    for i in range(len(s) - 2, -1, -1):
        # get the current character's value
        curr_no = roman_to_int[s[i]]
        # if the current value is less than the previous value, subtract it (eg IV: prev = 5, curr = 1)
        if curr_no < prev_no:
            total -= curr_no
        # otherwise, add it (eg VI: prev = 5, curr = 1)
        else:
            total += curr_no
        # update the previous value to the current value    
        prev_no = curr_no
    
    return total