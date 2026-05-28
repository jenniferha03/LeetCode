class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in valid:
                valid[i] += 1
            else:
                valid[i] = 1
        # a : 1
        # c : -1
        for i in t:
            if i in valid and valid[i] > 0:
                valid[i] -= 1
            else:
                return False
        return True
