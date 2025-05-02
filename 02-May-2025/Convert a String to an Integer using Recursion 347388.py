# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def str_to_int(s):
    if len(s) == 1:
        return ord(s[0]) - ord('0')
    
    first_dig = ord(s[0]) - ord('0')
    power = len(s) - 1
    res = first_dig * (10 ** power) + str_to_int(s[1:])
    return res


print(str_to_int("1235"))
print(str_to_int("1"))