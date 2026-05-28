class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        low = 0
        high = len(string) - 1
        while low < high:
            if string[low].lower() in vowels and string[high].lower() in vowels:
                string[low], string[high] = string[high], string[low]
                low += 1
                high -= 1
            elif string[low].lower() in vowels or string[high].lower() in vowels:
                if string[low].lower() in vowels:
                    high -= 1
                else:
                    low += 1
            else:
                low += 1
                high -= 1
        return "".join(string)