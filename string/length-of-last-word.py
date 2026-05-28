class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for letter in range(1, len(s)+1, 1):
            if s[len(s)-letter] != " ":
                length += 1
            elif length != 0:
                break
        return length