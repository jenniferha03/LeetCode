class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dictionary = []
        n = len(words)
        for idx, word in enumerate(words):
            temp_set = set()
            for char in word:
                temp_set.add(char)
            dictionary.append(temp_set)
        max_product = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if len(dictionary[i] & dictionary[j]) == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product