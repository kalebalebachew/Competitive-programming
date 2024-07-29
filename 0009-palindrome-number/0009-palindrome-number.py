class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the integer to a string
        str_x = str(x)

        # Check if the string is the same when read backward
        return str_x == str_x[::-1]
