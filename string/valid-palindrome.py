import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char
                new_str = new_str.lower() # abba
        for i in range(len(new_str)):
            if (new_str[i] != new_str[len(new_str)-i-1]):
                return False
        return True