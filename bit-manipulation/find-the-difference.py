class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashtable = {}
        for char in t:
            if char in hashtable:
                hashtable[char] += 1
            else:
                hashtable[char] = 1
        for char in s:
            if char in hashtable:
                hashtable[char] -= 1
            if hashtable[char] == 0:
                del hashtable[char]
        for key in hashtable.keys():
            return key