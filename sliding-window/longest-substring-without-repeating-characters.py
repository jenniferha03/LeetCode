class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        curr = 0
        for letter in range(len(s)):
            ptr = letter
            while ptr < len(s) and s[ptr] not in substr:
                substr.append(s[ptr])
                ptr += 1
            if len(substr) > curr:
                curr = len(substr)
            substr.clear()
        return curr