class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        special_cases = {
            'IV': 4, 'IX': 9, 'XL': 40,
            'XC': 90, 'CD': 400, 'CM': 900
        }
        
        i = 0
        total = 0
        length = len(s)
        
        while i < length:
            if i + 1 < length and s[i:i+2] in special_cases:
                total += special_cases[s[i:i+2]]
                i += 2
            else:
                total += roman_to_int[s[i]]
                i += 1
        
        return total




        
        