class Solution:
    def intToRoman(self, num: int) -> str:
        int_val = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_val = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

        result = ""

        # greedy approach by subtracting largest possible value each time 
        for integer, roman in zip(int_val, roman_val):
            while num >= integer:
                num -= integer
                result += roman
        
        return result