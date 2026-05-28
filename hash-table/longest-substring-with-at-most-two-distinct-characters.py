class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashtable = {}
        i = 0
        longest_sub = 0
        for j in range(len(s)): #j = 4, i = 3, longest_sub = 3, 
        #hash = {"b": 1, "a":1}         
            if s[j] not in hashtable:
                hashtable[s[j]] = 1
            else:
                hashtable[s[j]] += 1
            while len(hashtable) > 2: 
                hashtable[s[i]] -= 1
                if hashtable[s[i]] == 0:
                    del hashtable[s[i]]
                i += 1
            longest_sub = max(j-i+1, longest_sub)
        return longest_sub