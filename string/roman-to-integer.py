class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev = 0
        for char in s[::-1]:
            charVal = 0
            if char == "I":
                charVal = 1
            elif char == "V":
                charVal = 5
            elif char == "X":
                charVal = 10
            elif char == "L":
                charVal = 50
            elif char == "C":
                charVal = 100
            elif char == "D":
                charVal = 500
            else:
                charVal = 1000

            if charVal >= prev:
                total += charVal
            else:
                total -= charVal

            prev = charVal
        return total
        